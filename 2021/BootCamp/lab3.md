D: Local Temporary Storage, will delete data when deallocated or moved

**VM and Disks**
- https://github.com/hansenms/azure_templates
- protection with premium storage

**VMSS and Availability Sets**
VMSS: 
1. Virtual Machine Scale Sets 可以动态扩缩容的vm集群。
2. vm 会被放置在不同的rack上。
3. 上限100台
4. Fault Domains: 
- isolate virtual machines for faults, default 2.
- protect me from unplanned downtime.
5. Update Domains: 
- isolate virtual machines for upgrades, default 5 max 20.
- protect me from planned downtime.
- domain 指把机器划分成几个区域。

**Availability zones**
- 99.99%
- mutiple data centers

**Region pairs**
- protection from disaster with data residency compliance
- esatUS vs westUS
- one region have mutiple data centers

**CMD**
ipconfig /flushdns
nslookup contosoads-<alias>.centralus.cloudapp.azure.com

**psping tool**
psping is a network diagnostics tool that can be used to determine if ports on hosts are open
psping <webserverIPAddress>:3389

**CLI**
```
az login
az account set -s "<YourFTESubName>"
cd "C:\StudentFiles\Build It - Introduction to Azure IaaS - ARM"
az deployment group create -g "<alias>-rg" --template-file azuredeploy.sql.json --parameters "alias=<alias>" "adminPassword=demo@pass123"
az storage account create -g "<alias>-rg" -n "<alias>dsc" --sku Standard_LRS
az storage container create --account-name "<alias>dsc" -n dsc
az storage blob upload --account-name "<alias>dsc" -c dsc -f web-dsc-config.zip -n web-dsc-config.zip
# Retrieve a SAS token
az storage container generate-sas --account-name "<alias>dsc" -n dsc --permissions rw --expiry "2030-01-01"
az deployment group create -g "<alias>-rg" --template-file azuredeploy.web.json --parameters "alias=<alias>" "adminPassword=demo@pass123" "dscModulesUrl=https://<alias>dsc.blob.core.windows.net/dsc/web-dsc-config.zip?<sasToken>"
# Note: If you're using a PowerShell window instead of a Command Prompt window, you must add --% outside the quotes before the dscModulesUrl parameter. Failing to do so will cause PowerShell to interpret the & characters in the SAS token as chaining additional commands to execute, rather than interpreting it as a simple string value to pass along. Use the command below if you're executing from within a PowerShell command window:
az deployment group create -g "<alias>-rg" --template-file azuredeploy.web.json --parameters "alias=<alias>" "adminPassword=demo@pass123" --% "dscModulesUrl=https://<alias>dsc.blob.core.windows.net/dsc/web-dsc-config.zip?<sasToken>"
cd "C:\StudentFiles\Introduction to App Services - Web Apps"
az webapp deployment source config-zip --resource-group "<alias>-rg" --name "<alias>-webapp" --src "ContosoAds.Web.zip"
```