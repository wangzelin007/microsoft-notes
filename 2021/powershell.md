```
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
```