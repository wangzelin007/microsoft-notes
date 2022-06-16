https://github.com/Azure/azure-cli/issues/22732
https://github.com/Azure/azure-rest-api-specs/pull/18809/files
https://github.com/Azure/azure-rest-api-specs/pull/18786/files

PremiumV2_LRS

azure-mgmt-compute

az vm create --storage-sku 
az vmss create --storage-sku 
az vm disk attach --sku
az vmss disk attach --sku
需要顺带测试的：
az vm disk detach
az vmss disk detach

az disk create --sku
az disk update --sku
az image create --storage-sku

az snapshot create --sku 不支持

version:
Compute RP: 2022-03-01, 
Disk RP: 2022-03-02,
https://github.com/Azure/azure-rest-api-specs/pull/19116

C:\Code\azure-cli\src\azure-cli-core\azure\cli\core\profiles\_shared.py

PR:
{compute} Bump disk 2021-04-01 https://github.com/Azure/azure-cli/pull/20335/files
{Compute} Bump up azure-mgmt-compute SDK to 25.0.0 https://github.com/Azure/azure-cli/pull/21279

region: westus
az cloud set
az account set --subscription dd80b94e-0463-4a65-8d04-c94f403879dc

The 'PremiumV2_LRS' SKU is only supported for empty disks.

