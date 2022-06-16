az group create --location eastus2euap --name zelin62
失败
az vm create -g zelin62 -n vm-storage-sku-test --image UbuntuLTS --storage-sku os=Premium_LRS 0=Premium_LRS --debug xxx
cli.azure.cli.core.azclierror: Data disk with lun of '0' doesn't exist. Existing luns: dict_keys(['os']).
az_command_data_logger: Data disk with lun of '0' doesn't exist. Existing luns: dict_keys(['os']).
az vm create -g zelin62 -n vm-storage-sku-test --image UbuntuLTS --storage-sku os=Premium_LRS 0=Premium_LRS --data-disk-sizes-gb 10 --debug
az vm create -g zelin62 -n vm-storage-sku-test --image UbuntuLTS --storage-sku os=Premium_LRS 0=PremiumV2_LRS --debug xxx
az vm create -g zelin62 -n vm-storage-sku-test --admin-username admin123 --admin-password testPassword0 --image debian --storage-sku os=Premium_LRS 0=PremiumV2_LRS --data-disk-sizes-gb 10 --nsg-rule NONE --zone 2 --debug
az vm create -g zelin62 -n vm-storage-sku-test --admin-username admin123 --admin-password testPassword0 --image debian --storage-sku os=PremiumV2_LRS --data-disk-sizes-gb 1 --nsg-rule NONE
az vm create -g zelin62 -n vm-storage-sku-test --storage-sku PremiumV2_LRS --image UbuntuLTS --debug
az vm create -g zelin62 -n vm-storage-sku-test --storage-sku os=PremiumV2_LRS --image debian --debug XXX not support in os
az vm disk attach -g zelin62 --vm-name vm-storage-sku-test --name d2 --debug

Test Case1.1 TODO:
az group create --location eastus2euap --name zelin6
az vm create -g zelin62  -n vm-storage-sku-test --storage-sku Premium_LRS --image UbuntuLTS
az disk create -g zelin62 -n d2 --size-gb 10 --sku Premium_LRS --debug
az vm disk attach -g zelin62 --vm-name vm-storage-sku-test --name d2 --debug 

Test Case1.2 Done:
az group create --location eastus2euap --name zelin62
az vm create -g zelin62  -n vm-storage-sku-test --storage-sku Premium_LRS --image UbuntuLTS (success)
az disk create -g zelin62 -n d2 --size-gb 10 --sku PremiumV2_LRS --debug (success)
az vm disk attach -g zelin62 --vm-name vm-storage-sku-test --name d2 --debug (fail)

Test Case2 Done:
az group create --location eastus2euap --name zelin62
az vm create -g zelin62 -n vm-storage-sku-test --image UbuntuLTS --storage-sku os=Premium_LRS 0=Premium_LRS --data-disk-sizes-gb 10 --debug (success)
az vm create -g zelin62 -n vm-storage-sku-test2 --image UbuntuLTS --storage-sku os=Premium_LRS 0=PremiumV2_LRS --data-disk-sizes-gb 10 --debug (fail)

Test Case3 Done:
az group create --location eastus2euap --name zelin62
az vm create -g zelin62 -n vm-storage-sku-test3 --image UbuntuLTS --storage-sku os=Premium_LRS 0=Premium_LRS --data-disk-sizes-gb 10 --zone 1 --debug (success)
az vm create -g zelin62 -n vm-storage-sku-test4 --image UbuntuLTS --storage-sku os=Premium_LRS 0=PremiumV2_LRS --data-disk-sizes-gb 10 --zone 1 --debug (success)
az disk create -g zelin62 -n d3 --size-gb 10 --sku PremiumV2_LRS --zone 1 (success)
az vm disk attach -g zelin62 --vm-name vm-storage-sku-test4 --name d3 --debug (success)

Test Case4 VMSS:
az group create --location eastus2euap --name zelin62

az vmss create -g zelin62 -n vmss-storage-sku-test --image UbuntuLTS --storage-sku os=Premium_LRS 0=PremiumV2_LRS --data-disk-sizes-gb 10 --zone 1 --debug (fail)
az vmss create -g zelin62 -n vmss-storage-sku-test --image UbuntuLTS --zone 1
az disk create -g zelin62 -n d1 --size-gb 10 --sku PremiumV2_LRS --zone 1 
az vmss disk attach -g zelin62 --vmss-name vmss-storage-sku-test --disk d1 --instance-id 0 --debug (fail)
az disk create -g zelin62 -n d2 --size-gb 10 --sku Premium_LRS --zone 1
az vmss disk attach -g zelin62 --vmss-name vmss-storage-sku-test --disk d2 --instance-id 1 --debug

az vmss create --resource-group zelin62 --name vmss-storage-sku-test2 --image UbuntuLTS --vm-sku Standard_DS4_v2 --instance-count 2 --data-disk-sizes-gb 10 --storage-sku os=standard_lrs 0=Premium_LRS --debug (success)
az vmss create --resource-group zelin62 --name vmss-storage-sku-test3 --image UbuntuLTS --vm-sku Standard_DS4_v2 --instance-count 2 --data-disk-sizes-gb 10 --storage-sku os=standard_lrs 0=PremiumV2_LRS --debug (fail)
az vmss create --resource-group zelin62 --name vmss-storage-sku-test3 --image UbuntuLTS --vm-sku Standard_DS4_v2 --instance-count 2 --data-disk-sizes-gb 10 --storage-sku os=standard_lrs 0=PremiumV2_LRS --zone 1 --debug
az vmss create --resource-group zelin62 --name vmss-storage-sku-test3 --image UbuntuLTS --vm-sku Standard_DS4_v2 --instance-count 2 --data-disk-sizes-gb 10 --storage-sku os=standard_lrs 0=PremiumV2_LRS --zone 2 --debug
az vmss create --resource-group zelin62 --name vmss-storage-sku-test3 --image UbuntuLTS --vm-sku Standard_DS4_v2 --instance-count 2 --data-disk-sizes-gb 10 --storage-sku os=standard_lrs 0=PremiumV2_LRS --zone 3 --debug