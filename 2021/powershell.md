```
powershell + azure
https://docs.microsoft.com/en-us/powershell/azure/install-az-ps?view=azps-6.5.0
https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.2
Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force
$PSVersionTable.PSVersion

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

```cmd
mklink /j "C:\Users\zelinwang\Anaconda3\envs\azdev-20211109-3\Lib\site-packages\azdev" "D:\code\azure-cli-dev-tools\azdev"
mklink /j "C:\Users\zelinwang\OneDrive - Microsoft\D" "D:\"
```