#!/usr/bin/env bash

set -ev

# Create the auto_merge.py Python script file
cat >auto_merge.py <<EOL
#!/usr/bin/env python

import argparse
import glob
import mimetypes
import os
from typing import Iterable

from azure.storage.blob import BlobServiceClient, ContentSettings

INDEX_NAME = 'simple'
# Network connection timeout
TIMEOUT = 120


def generate_package_list_in_html(title: str, links: Iterable):
    package_list = '\n'.join((f'    <a href="{p}">{p}</a><br />' for p in links))
    return f"""<html>
<head>
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
{package_list}
</body>
</html>"""


def publish(dist: str, account: str, container: str, credential: str) -> None:
    account_url = f"https://{account}.blob.core.windows.net"
    service_client = BlobServiceClient(account_url=account_url, credential=credential, connection_timeout=TIMEOUT)
    container_client = service_client.get_container_client(container)

    modules_list = []
    container_url = f"{account_url}/{container}"
    print(f"Uploading {dist} to {container_url}")
    for wheel_file in glob.iglob(os.path.join(dist, '*.whl')):
        base_wheel_name = os.path.basename(wheel_file)  # azure_cli-2.17.0-py3-none-any.whl
        package_name = base_wheel_name.split('-', maxsplit=1)[0].replace('_', '-')  # azure-cli
        sdist_file = next(glob.iglob(os.path.join(dist, f'{package_name}-[0-9]*.tar.gz')))  # .../pypi/azure-cli-2.17.0.tar.gz
        blob_prefix = f'{INDEX_NAME}/{package_name}'  # simple/azure-cli

        content_type, content_encoding = mimetypes.guess_type(os.path.basename(wheel_file))
        content_settings = ContentSettings(content_type, content_encoding)

        print(package_name)
        # Upload wheel
        print(f"  {base_wheel_name} -> {blob_prefix}/{base_wheel_name}")
        with open(wheel_file, "rb") as data:
            container_client.upload_blob(f'{blob_prefix}/{base_wheel_name}',
                                         data, content_settings=content_settings, overwrite=True)

        base_sdist_name = os.path.basename(sdist_file)  # azure-cli-2.17.0.tar.gz
        content_type, content_encoding = mimetypes.guess_type(os.path.basename(sdist_file))
        content_settings = ContentSettings(content_type, content_encoding)

        # Upload sdist
        print(f"  {base_sdist_name} -> {blob_prefix}/{base_sdist_name}")
        with open(sdist_file, "rb") as data:
            container_client.upload_blob(f'{blob_prefix}/{base_sdist_name}',
                                         data, content_settings=content_settings, overwrite=True)

        package_blobs = (os.path.basename(b.name)
                         for b in container_client.list_blobs(name_starts_with=f'{blob_prefix}/')
                         if b.name != f"{blob_prefix}/")

        # Create project-file index
        print(f"  Create project-file index: {container_url}/{blob_prefix}/")
        container_client.upload_blob(f'{blob_prefix}/',
                                     data=generate_package_list_in_html(f'Links for {package_name}', package_blobs),
                                     content_settings=ContentSettings('text/html'), overwrite=True)

        modules_list.append(f"{package_name}/")

    # Create repository-project index
    print(f"Create repository-project index: {container_url}/{INDEX_NAME}/")
    container_client.upload_blob(f'{INDEX_NAME}/',
                                 data=generate_package_list_in_html('Simple Index', modules_list),
                                 content_settings=ContentSettings('text/html'), overwrite=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='az-publish', description='Publish Python build artifacts to Azure Storage Account and create PEP 503 index.')

    parser.add_argument('--dist', '-d', help='The folder where the artifacts are saved.')
    parser.add_argument('--account', '-a', help='The storage account name.')
    parser.add_argument('--container', '-c', help='The storage account container.')
    parser.add_argument('--credential', help='SAS token string or Storage Account shared access key.')

    args = parser.parse_args()
    publish(args.dist, args.account, args.container, args.credential)
EOL

# Show Azure CLI verison
az --version

# List all artifacts
ls --recursive

account=$1
container=$2
# https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html
dist=${3:-${SYSTEM_ARTIFACTSDIRECTORY}/_Azure.azure-cli/pypi}

# Fetch Storage Account key
key=$(az storage account keys list --account-name $account --query [0].value --output tsv)

# Intall azure-storage-blob SDK
pip3 install azure-storage-blob~=12.6.0

python3 publish_az.py --dist $dist --account $account --container $container --credential "$key"

rm publish_az.py

################################

echo $(pwd)

# git config
GITHUB_TOKEN=$(az keyvault secret show --vault-name kv-azuresdk --name azclibot-pat --query value -otsv)

git config --global user.email "AzPyCLI@microsoft.com"
git config --global user.name "Azure CLI Team"

git remote add azclibot https://azclibot:${GITHUB_TOKEN}@github.com/azclibot/azure-cli-extensions.git

git status

#touch upgrade_extensions.txt
#echo "virtual-wan" >> upgrade_extensions.txt
#echo "storage-preview" >> upgrade_extensions.txt

#######################
# prepare
#######################

upgraded_extensions=""
for extension in $(cat upgrade_extensions.txt)
do
    ext=`echo $extension | sed -e 's/\n//'`
    upgraded_extensions+="[ $ext ] "
done

extension_commit_id="$(Build.SourceVersion)"

commit_url="https://github.com/Azure/azure-cli-extensions/commit/${extension_commit_id}"
commit_msg_title="[Release] Update index.json for extension $upgraded_extensions"
commit_msg_body="Triggered by Azure CLI Extensions Release Pipeline - ADO_BUILD_ID=$(Build.BuildId)"
commit_msg="${commit_msg_title}\n\n ${commit_msg_body}\n\nLast commit against main: ${commit_url}"


#######################
# save branch
#######################

temp_branch="release-$(date +%Y%m%d-%H%M%S)"
git checkout -b "$temp_branch"
git add .
git commit -m "${commit_msg_title}" -m "${commit_msg_body}" -m "Last commit: ${commit_url}"
git push -u azclibot "$temp_branch"


#######################
# ceate PR
#######################

pr_title="$commit_msg_title"
pr_body="$commit_msg"
pr_head="azclibot:${temp_branch}"

curl \
-H "Authorization: token ${GITHUB_TOKEN}" \
-d "{\"title\": \"${pr_title}\", \"body\": \"${pr_body}\", \"head\": \"${pr_head}\", \"base\": \"test-auto-merge\"}" \
https://api.github.com/repos/Azure/azure-cli-extensions/pulls > /tmp/create_pr.json
