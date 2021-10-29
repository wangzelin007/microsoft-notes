```
powershell + azure
https://docs.microsoft.com/en-us/powershell/azure/install-az-ps?view=azps-6.5.0
New-AzVirtualNetwork -?
To see the examples, type: "Get-Help New-AzVirtualNetwork -Examples"
For more information, type: "Get-Help New-AzVirtualNetwork -Detailed"
For technical information, type: "Get-Help New-AzVirtualNetwork -Full"
For online help, type: "Get-Help New-AzVirtualNetwork -Online"

"`nNew-Alias which get-command" | add-content $profile
C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1
"`nNew-Alias which get-command" | add-content C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1
get-command az

**grep**
az vm update --help|findstr 'or'
netstat -na | Select-String "PORT"

**which**
get-command python

**wc -l**
pip list|Measure-Object -line

**rm**
Remove-Item C:\tmp -Recurse -Force
```