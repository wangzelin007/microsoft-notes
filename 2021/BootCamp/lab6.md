**Azure App Service**
App Service: Azure Web App sandbox and/or Docker container.
App Service plan: Collection of virtual machines hosting a set of Azure Web App sandboxes or Docker containers.

Vertical Scaling: 
- scaling up/down
- larger VM size or maller VM size
- temporarily unabailable because redeployed.

Horizontal Scaling:
- scaling out/in
- without interruption

```
cd "C:\StudentFiles\Introduction to App Services - Web Apps"
Compress-Archive -Path .\ContosoAds.Web\* -DestinationPath ContosoAds.Web.zip
Server=tcp:zeli62-westeurope-sql.database.windows.net,1433;Initial Catalog=ContosoAds;Persist Security Info=False;User ID=demouser;Password={your_password};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;
```