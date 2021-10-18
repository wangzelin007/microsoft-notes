Learning Objectives

In this lab module, you will learn to manage Azure resources using three different tools - the Azure Portal, Powershell and Azure CLI.  
You will create a resource group to contain the resources you create in the boot camp.  
You will set a subscription filter to use the prescribed subscription for the boot camp.  
You will also access your resource group using both Powershell and Azure CLI.  

1. You will access the Azure Portal using your Personal credentials
2. You will add a subscription filter so that the free Azure subscription you have as a Microsoft full-time employee will be applied to all resources you create for the boot camp
3. You will create a resource group. You will use this resource group to contain all the resources you create for the boot camp
4. You will use Powershell to list the resource groups in your subscription
```
Connect-AzAccount
Connect-AzAccount -DeviceCode # pormpt you to open a website
Get-AzSubscription -SubscriptionName "<YourFTESubName>"
Select-AzSubscription -SubscriptionId <YourFTESubID>
Get-AzResourceGroup
```
5. You will use Azure CLI to list the resource groups in your subscription
```
az login
az account set -s "<YourFTESubName>"
az group list
```

You can find more information on these tools at:  
Azure Portal: https://azure.microsoft.com/en-us/features/azure-portal/  
Powershell: https://docs.microsoft.com/en-us/powershell/azure/overview  
Azure CLI: https://docs.microsoft.com/en-us/cli/azure/?view=azure-cli-latest  

**Pin** your new Resource Group to your Azure Portal Dashboard so that you can easily locate resources in future labs.  
Select the pin icon in the top left corner of your Resource Group windows.  