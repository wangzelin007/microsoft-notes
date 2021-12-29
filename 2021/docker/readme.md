[comment]: <> ( microdnf install yum)
yum check-update ; yum install -y vim gcc libffi-devel python3 openssl-devel

[comment]: <> (curl -L https://aka.ms/InstallAzureCli | bash)
dnf install azure-cli

dnf install 失败

-------
curl 'https://artprodcus3.artifacts.visualstudio.com/A0fb41ef4-5012-48a9-bf39-4ee3de03ee35/29ec6040-b234-4e31-b139-33dc4287b756/_apis/artifact/cGlwZWxpbmVhcnRpZmFjdDovL2F6dXJlLXNkay9wcm9qZWN0SWQvMjllYzYwNDAtYjIzNC00ZTMxLWIxMzktMzNkYzQyODdiNzU2L2J1aWxkSWQvMTI2NzE1OS9hcnRpZmFjdE5hbWUveXVt0/content?format=file&subPath=%2Fazure-cli-2.31.0-1.el7.x86_64.rpm' -o azure-cli.rpm

curl https://packages.microsoft.com/yumrepos/azure-cli/azure-cli-2.31.0-1.el7.x86_64.rpm -O

rpm --checksig --verbose azure-cli-2.31.0-1.el7.x86_64.rpm
rpm --checksig -v azure-cli-2.31.0-1.el7.x86_64.rpm