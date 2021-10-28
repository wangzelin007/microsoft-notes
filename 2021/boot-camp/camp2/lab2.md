```
cd C:\repos\Bootcamp\ContosoAdsSupport
git pull
git reset --hard lab/start
git checkout -b feature/<alias>
az account set -s "Azure Boot Camp (Alpha)"
az cosmosdb keys list --type connection-strings --name contososupport --resource-group architecture
start C:\repos\Bootcamp\ContosoAdsSupport\src\ContosoAdsSupport\ContosoSupport.sln
git add src\ContosoAdsSupport\ContosoSupport\appsettings.json
git commit -m "Committing the connection string"
git push -u origin feature/<alias>

Undo your changes
git status
git reset HEAD src\ContosoAdsSupport\ContosoSupport\appsettings.json
git status
git checkout src\ContosoAdsSupport\ContosoSupport\appsettings.json
git status
```

Branching:
git branch

Fetching Source:
git pull
git fetch

Undoing Changes:
git reset
git checkout
git revert
git clean

Moving Code Around:
git rebase
git merge
git cherry-pick
