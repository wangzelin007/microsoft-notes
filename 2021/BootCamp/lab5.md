**Azure Storage**
Blob Storage: Blobs
- Unstructured data
- Scenarios include document, images, videos, logs, backup files, etc.
File Service: Files and Folders
- Mount file shares from VMs in Azure or on-premises
Table Storage: Entities
- Store flexible datasets that are not constrained by a schema
- Entity is a name-value pair
Queue Storage: Messages
- Creating a backlog of work to process asynchronously
- asynchronous communication between decoupled application components

```
az login
az account set -s "<YourBootCampSubName>"
az sql server create --name "<alias>-westeurope-sql" --resource-group "<alias>-rg" --location "westeurope" --admin-user "demouser" --admin-password "demo@pass123"
az sql server firewall-rule create --resource-group "<alias>-rg" --server "<alias>-westeurope-sql" --name "Allow Azure services" --start-ip-address 0.0.0.0 --end-ip-address 0.0.0.0
az sql db create --resource-group "<alias>-rg" --server "<alias>-westeurope-sql" --name "ContosoAds" --edition "Basic"
az storage account create --name "<alias>storage" --resource-group "<alias>-rg" --location "westeurope" --access-tier "Hot" --kind "StorageV2" --sku "Standard_LRS"
```