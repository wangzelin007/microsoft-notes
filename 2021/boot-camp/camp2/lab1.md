```
az extension add --name azure-devops
az login
if not exist C:\repos mkdir C:\repos
cd C:\repos
git clone https://onebranch.visualstudio.com/Bootcamp/_git/ContosoAdsSupport/ Bootcamp\ContosoAdsSupport
cd C:\repos\Bootcamp\ContosoAdsSupport
git checkout lab/start
git pull
```