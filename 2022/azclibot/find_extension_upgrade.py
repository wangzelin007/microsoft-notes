# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import sys
import json
from subprocess import check_output
from pkg_resources import parse_version


def separator_line():
    print('-' * 100)


class AzdevExtensionHelper:
    def __init__(self, extension_name):
        self.name = extension_name

    def is_version_upgrade(self):
        with open('src/index.json') as fd:
            current_extensions = json.loads(fd.read()).get("extensions")

        # src/desktopvirtualization/setup.py
        setup_py = 'src/{}/setup.py'.format(self.name)

        if os.path.isfile(setup_py) is False:
            print('no setup.py')
            return False

        # python setup.py --name: desktopvirtualization
        cmd = sys.executable + ' setup.py --name'
        self.name = check_output(cmd, shell=True, cwd=os.path.dirname(setup_py)).decode('utf-8').strip()
        self.name = self.name.replace('_', '-')

        metadata = current_extensions.get(self.name, None)
        if metadata is None:    # for new added extension
            return True

        # get latest version
        current_max_entry = max(metadata, key=lambda e: parse_version(e['metadata']['version']))
        # 0.2.0
        current_max_version = current_max_entry['metadata']['version']
        print('current max version is {}'.format(current_max_version))

        # python setup.py --version
        cmd = sys.executable + ' setup.py --version'
        # 0.2.0
        modified_version = check_output(cmd, shell=True, cwd=os.path.dirname(setup_py)).decode('utf-8').strip()
        print('modified version is {}'.format(modified_version))

        if parse_version(current_max_version) > parse_version(modified_version):
            err = 'version downgrade is not allowed in extension {0}. [{1} -> {2}]'.format(setup_py,
                                                                                           current_max_version,
                                                                                           modified_version)
            raise Exception(err)
        if parse_version(current_max_version) == parse_version(modified_version):
            return False

        return True


def find_modified_files_against_master_branch():
    """
    Deleted files don't count in diff
    """
    cmd = 'git --no-pager diff --diff-filter=ACMRT --name-only HEAD~1 -- src/'
    # src/desktopvirtualization/setup.cfg
    # src/desktopvirtualization/setup.py
    # files = check_output(cmd.split()).decode('utf-8').split('\n')
    files = ['src/desktopvirtualization/setup.cfg', 'src/desktopvirtualization/setup.py']

    separator_line()
    print('modified files:')
    for f in files:
        print(f)
    separator_line()

    return [f for f in files if len(f) > 0]


def contain_extension_code(files):
    with open('src/index.json', 'r') as fd:
        # dict 128
        # {
        #     "account": [
        #         {
        #             "downloadUrl": "https://azurecliprod.blob.core.windows.net/cli-extensions/account-0.1.0-py2.py3-none-any.whl",
        #             "filename": "account-0.1.0-py2.py3-none-any.whl",
        #             "metadata": {
        #                 "azext.isExperimental": true,
        #                 "azext.minCliCoreVersion": "2.3.1",
        #                 "classifiers": [
        #                     "Development Status :: 4 - Beta",
        #                     "Intended Audience :: Developers",
        #                     "Intended Audience :: System Administrators",
        #                     "Programming Language :: Python",
        #                     "Programming Language :: Python :: 3",
        #                     "Programming Language :: Python :: 3.6",
        #                     "Programming Language :: Python :: 3.7",
        #                     "Programming Language :: Python :: 3.8",
        #                     "License :: OSI Approved :: MIT License"
        #                 ],
        #                 "extensions": {
        #                     "python.details": {
        #                         "contacts": [
        #                             {
        #                                 "email": "azpycli@microsoft.com",
        #                                 "name": "Microsoft Corporation",
        #                                 "role": "author"
        #                             }
        #                         ],
        #                         "document_names": {
        #                             "description": "DESCRIPTION.rst"
        #                         },
        #                         "project_urls": {
        #                             "Home": "https://github.com/Azure/azure-cli-extensions"
        #                         }
        #                     }
        #                 },
        #                 "generator": "bdist_wheel (0.30.0)",
        #                 "license": "MIT",
        #                 "metadata_version": "2.0",
        #                 "name": "account",
        #                 "summary": "Microsoft Azure Command-Line Tools SubscriptionClient Extension",
        #                 "version": "0.1.0"
        #             },
        #             "sha256Digest": "badd35099d52efc5d8c337eee3ce3958005e6bfbb0c83798a74458b90ea6046b"
        #         },
        #         {
        #             "downloadUrl": "https://azurecliprod.blob.core.windows.net/cli-extensions/account-0.2.0-py2.py3-none-any.whl",
        #             "filename": "account-0.2.0-py2.py3-none-any.whl",
        #             "metadata": {
        #                 "azext.isExperimental": true,
        #                 "azext.minCliCoreVersion": "2.3.1",
        #                 "classifiers": [
        #                     "Development Status :: 4 - Beta",
        #                     "Intended Audience :: Developers",
        #                     "Intended Audience :: System Administrators",
        #                     "Programming Language :: Python",
        #                     "Programming Language :: Python :: 3",
        #                     "Programming Language :: Python :: 3.6",
        #                     "Programming Language :: Python :: 3.7",
        #                     "Programming Language :: Python :: 3.8",
        #                     "License :: OSI Approved :: MIT License"
        #                 ],
        #                 "extensions": {
        #                     "python.details": {
        #                         "contacts": [
        #                             {
        #                                 "email": "azpycli@microsoft.com",
        #                                 "name": "Microsoft Corporation",
        #                                 "role": "author"
        #                             }
        #                         ],
        #                         "document_names": {
        #                             "description": "DESCRIPTION.rst"
        #                         },
        #                         "project_urls": {
        #                             "Home": "https://github.com/Azure/azure-cli-extensions"
        #                         }
        #                     }
        #                 },
        #                 "generator": "bdist_wheel (0.30.0)",
        #                 "license": "MIT",
        #                 "metadata_version": "2.0",
        #                 "name": "account",
        #                 "summary": "Microsoft Azure Command-Line Tools SubscriptionClient Extension",
        #                 "version": "0.2.0"
        #             },
        #             "sha256Digest": "a5613056e59cccaf4de58d9b108b0103f1b5a698345e6261b5bf83b3ff7637cf"
        #         },
        #         {
        #             "downloadUrl": "https://azurecliprod.blob.core.windows.net/cli-extensions/account-0.2.1-py3-none-any.whl",
        #             "filename": "account-0.2.1-py3-none-any.whl",
        #             "metadata": {
        #                 "azext.isExperimental": true,
        #                 "azext.minCliCoreVersion": "2.3.1",
        #                 "classifiers": [
        #                     "Development Status :: 4 - Beta",
        #                     "Intended Audience :: Developers",
        #                     "Intended Audience :: System Administrators",
        #                     "Programming Language :: Python",
        #                     "Programming Language :: Python :: 3",
        #                     "Programming Language :: Python :: 3.6",
        #                     "Programming Language :: Python :: 3.7",
        #                     "Programming Language :: Python :: 3.8",
        #                     "License :: OSI Approved :: MIT License"
        #                 ],
        #                 "extensions": {
        #                     "python.details": {
        #                         "contacts": [
        #                             {
        #                                 "email": "azpycli@microsoft.com",
        #                                 "name": "Microsoft Corporation",
        #                                 "role": "author"
        #                             }
        #                         ],
        #                         "document_names": {
        #                             "description": "DESCRIPTION.rst"
        #                         },
        #                         "project_urls": {
        #                             "Home": "https://github.com/Azure/azure-cli-extensions/tree/master/src/account"
        #                         }
        #                     }
        #                 },
        #                 "generator": "bdist_wheel (0.30.0)",
        #                 "license": "MIT",
        #                 "metadata_version": "2.0",
        #                 "name": "account",
        #                 "summary": "Microsoft Azure Command-Line Tools SubscriptionClient Extension",
        #                 "version": "0.2.1"
        #             },
        #             "sha256Digest": "aba36f7a6f109d2bd1b1624ebcfdfd07a97e9a0b05b051d0af7d2ddb4d2f3c89"
        #         },
        #         {
        #             "downloadUrl": "https://azcliprod.blob.core.windows.net/cli-extensions/account-0.2.2-py3-none-any.whl",
        #             "filename": "account-0.2.2-py3-none-any.whl",
        #             "metadata": {
        #                 "azext.isExperimental": true,
        #                 "azext.minCliCoreVersion": "2.3.1",
        #                 "classifiers": [
        #                     "Development Status :: 4 - Beta",
        #                     "Intended Audience :: Developers",
        #                     "Intended Audience :: System Administrators",
        #                     "Programming Language :: Python",
        #                     "Programming Language :: Python :: 3",
        #                     "Programming Language :: Python :: 3.6",
        #                     "Programming Language :: Python :: 3.7",
        #                     "Programming Language :: Python :: 3.8",
        #                     "License :: OSI Approved :: MIT License"
        #                 ],
        #                 "extensions": {
        #                     "python.details": {
        #                         "contacts": [
        #                             {
        #                                 "email": "azpycli@microsoft.com",
        #                                 "name": "Microsoft Corporation",
        #                                 "role": "author"
        #                             }
        #                         ],
        #                         "document_names": {
        #                             "description": "DESCRIPTION.rst"
        #                         },
        #                         "project_urls": {
        #                             "Home": "https://github.com/Azure/azure-cli-extensions/tree/main/src/account"
        #                         }
        #                     }
        #                 },
        #                 "generator": "bdist_wheel (0.30.0)",
        #                 "license": "MIT",
        #                 "metadata_version": "2.0",
        #                 "name": "account",
        #                 "summary": "Microsoft Azure Command-Line Tools SubscriptionClient Extension",
        #                 "version": "0.2.2"
        #             },
        #             "sha256Digest": "adffb8a4ceaecde0157467740551cea2b983ae5483d9b0ec59f9c678f232066d"
        #         },
        #         {
        #             "downloadUrl": "https://azcliprod.blob.core.windows.net/cli-extensions/account-0.2.3-py3-none-any.whl",
        #             "filename": "account-0.2.3-py3-none-any.whl",
        #             "metadata": {
        #                 "azext.minCliCoreVersion": "2.3.1",
        #                 "classifiers": [
        #                     "Development Status :: 4 - Beta",
        #                     "Intended Audience :: Developers",
        #                     "Intended Audience :: System Administrators",
        #                     "Programming Language :: Python",
        #                     "Programming Language :: Python :: 3",
        #                     "Programming Language :: Python :: 3.6",
        #                     "Programming Language :: Python :: 3.7",
        #                     "Programming Language :: Python :: 3.8",
        #                     "License :: OSI Approved :: MIT License"
        #                 ],
        #                 "extensions": {
        #                     "python.details": {
        #                         "contacts": [
        #                             {
        #                                 "email": "azpycli@microsoft.com",
        #                                 "name": "Microsoft Corporation",
        #                                 "role": "author"
        #                             }
        #                         ],
        #                         "document_names": {
        #                             "description": "DESCRIPTION.rst"
        #                         },
        #                         "project_urls": {
        #                             "Home": "https://github.com/Azure/azure-cli-extensions/tree/main/src/account"
        #                         }
        #                     }
        #                 },
        #                 "generator": "bdist_wheel (0.30.0)",
        #                 "license": "MIT",
        #                 "metadata_version": "2.0",
        #                 "name": "account",
        #                 "summary": "Microsoft Azure Command-Line Tools SubscriptionClient Extension",
        #                 "version": "0.2.3"
        #             },
        #             "sha256Digest": "94aa62990cc1260c24100501c3479d0f1ddbb485dccdbecf42228382c537f019"
        #         }
        #     ]
        # }
        current_extensions = json.loads(fd.read()).get("extensions")

    # set 128
    # {src/account, xxx}
    current_extension_homes = set('src/{}'.format(name) for name in current_extensions)

    for file in files:
        if any([file.startswith(prefix) for prefix in current_extension_homes]):
            return True

    # for new added extensions
    for file in files:
        if 'src/' in file and os.path.isfile(file) and os.path.isdir(os.path.dirname(file)):
            new_extension_home = os.path.dirname(file)

            new_extension_home = os.path.join(*new_extension_home.split('/')[:2])

            if os.path.isfile(os.path.join(new_extension_home, 'setup.py')):
                return True

    return False


def main():
    modified_files = find_modified_files_against_master_branch()

    if 'src/index.json' in modified_files:
        modified_files.remove('src/index.json')

    if not contain_extension_code(modified_files):
        separator_line()
        print('no extension source code is modified, no need to publish')
        separator_line()
        return

    extension_names = set()

    for f in modified_files:
        # src, desktopvirtulization, ['setup.cfg']
        src, name, *_ = f.split('/')
        if os.path.isdir(os.path.join(src, name)):
            extension_names.add(name)

    for name in extension_names:
        azdev_extension = AzdevExtensionHelper(name)

        if azdev_extension.is_version_upgrade() is False:
            print('extension [{}] is not upgrade, no need to help publish'.format(name))
            continue

        with open('./upgrade_extensions.txt', 'a') as fd:
            fd.write(name + '\n')


if __name__ == '__main__':
    main()
