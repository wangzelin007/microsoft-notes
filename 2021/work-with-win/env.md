cmd:
set DEBUG=true

powershell:
$Env:DEBUG = "true"
ls env:

[comment]: <> (import os path=r"E:\env" command =r"setx WORK1 %s /m"%path os.system&#40;command&#41;)
[environment]::GetEnvironmentvariable("AZURE_CLI_TEST_COMMAND_COVERAGE", "User")
[environment]::GetEnvironmentvariable("azure_client_secret", "User")
[environment]::SetEnvironmentvariable("变量名称", "变量值", "User")
[environment]::SetEnvironmentvariable("AZURE_CLI_TEST_COMMAND_COVERAGE", "True", "User")

python:
import os
os.environ['AZURE_CLI_TEST_COMMAND_COVERAGE']="True"
os.environ
{
  "ALLUSERSPROFILE": "C:\\ProgramData",
  "APPDATA": "C:\\Users\\zelinwang\\AppData\\Roaming",
  "CHASSIS": "Notebook",
  "COMMONPROGRAMFILES": "C:\\Program Files\\Common Files",
  "COMMONPROGRAMFILES(X86)": "C:\\Program Files (x86)\\Common Files",
  "COMMONPROGRAMW6432": "C:\\Program Files\\Common Files",
  "COMPUTERNAME": "LOCAL-VTKPMNF0G",
  "COMSPEC": "C:\\Windsers\\zelinwang",
  "LOCALAPPDATA": "C:\\Users\\zelinwang\\AppData\\Local",
  "LOGONSERVER": "\\\\LOCAL-VTKPMNF0G",
  "MODEL": "5420",
  "NUMBER_OF_PROCESSORS": "8",
  "ONEDRIVE": "C:\\Users\\zelinwang\\OneDrive - Microsoft",
  "ONEDRIVECOMMERCIAL": "C:\\Users\\zelinwang\\OneDrive - Microsoft",
  "OS": "Windows_NT",
  "PATH": "C:\\Code\\azure-cli-dev-tools\\env\\Scripts;C:\\Program Files\\PowerShell\\7;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files\\PowerShell\\7\\;C:\\Program Files\\Git\\cmd;C:\\Program Files\\nodejs\\;C:\\Users\\zelinwang\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\;C:\\Users\\zelinwang\\AppData\\Local\\Programs\\Python\\Python39\\;C:\\Users\\zelinwang\\AppData\\Local\\GitHubDesktop\\bin;C:\\Program Files\\JetBrains\\PyCharm2021.2.3\\bin;C:\\Users\\zelinwang\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\zelinwang\\AppData\\Roaming\\npm;C:\\Users\\zelinwang\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Code",
  "PATHEXT": ".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.CPL",
  "POWERSHELL_DISTRIBUTION_CHANNEL": "MSI:Windows 10 Enterprise",
  "PROCESSOR_ARCHITECTURE": "AMD64",
  "PROCESSOR_IDENTIFIER": "Intel64 Family 6 Model 140 Stepping 1, GenuineIntel",
  "PROCESSOR_LEVEL": "6",
  "PROCESSOR_REVISION": "8c01",
  "PROGRAMDATA": "C:\\ProgramData",
  "PROGRAMFILES": "C:\\Program Files",
  "PROGRAMFILES(X86)": "C:\\Program Files (x86)",
  "PROGRAMW6432": "C:\\Program Files",
  "PSMODULEPATH": "C:\\Users\\zelinwang\\OneDrive - Microsoft\\Documents\\PowerShell\\Modules;C:\\Program Files\\PowerShell\\Modules;c:\\program files\\powershell\\7\\Modules;C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules;C:\\Program Files (x86)\\Microsoft Azure Information Protection\\Powershell",
  "PUBLIC": "C:\\Users\\Public",
  "PYCHARM COMMUNITY EDITION": "C:\\Program Files\\JetBrains\\PyCharm2021.2.3\\bin;",
  "SERIAL": "HQFBGK3",
  "SYSTEMDRIVE": "C:",
  "SYSTEMROOT": "C:\\Windows",
  "TEMP": "C:\\Users\\ZELINW~1\\AppData\\Local\\Temp",
  "TMP": "C:\\Users\\ZELINW~1\\AppData\\Local\\Temp",
  "TYPE": "LATITUDE",
  "USERDNSDOMAIN": "fareast.corp.microsoft.com",
  "USERDOMAIN": "FAREAST",
  "USERDOMAIN_ROAMINGPROFILE": "FAREAST",
  "USERNAME": "zelinwang",
  "USERPROFILE": "C:\\Users\\zelinwang",
  "VIRTUAL_ENV": "C:\\Code\\azure-cli-dev-tools\\env",
  "WINDIR": "C:\\Windows",
  "WSLENV": "WT_SESSION::WT_PROFILE_ID",
  "WT_PROFILE_ID": "{574e775e-4f2a-5b96-ac1e-a2962a402336}",
  "WT_SESSION": "3a9f3703-3d5a-4fc9-a707-cd3f1230200a",
  "ZES_ENABLE_SYSMAN": "1",
  "_OLD_VIRTUAL_PATH": "C:\\Program Files\\PowerShell\\7;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files\\PowerShell\\7\\;C:\\Program Files\\Git\\cmd;C:\\Program Files\\nodejs\\;C:\\Users\\zelinwang\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\;C:\\Users\\zelinwang\\AppData\\Local\\Programs\\Python\\Python39\\;C:\\Users\\zelinwang\\AppData\\Local\\GitHubDesktop\\bin;C:\\Program Files\\JetBrains\\PyCharm2021.2.3\\bin;C:\\Users\\zelinwang\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\zelinwang\\AppData\\Roaming\\npm;C:\\Users\\zelinwang\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Code"
}

.env:
DEBUG=true
DATABASE_URL=sqlite:///mydb.sqlite
pip install python-dotenv
>>> from dotenv import load_dotenv
>>> load_dotenv()
>>> from dotenv import load_dotenv
>>> load_dotenv('/home/miguel/my_project/.env')