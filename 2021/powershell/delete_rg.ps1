$rgs = az group list | ConvertFrom-Json
Write-Output $rgs.name
Write-Output $rgs.Count
# dry run
$rgs | ForEach-Object { Write-Host "deleteing" $_.name}
$rgs | ForEach-Object -Parallel { Write-Host "deleteing" $_.name; az group delete --name $_.name --yes --no-wait }