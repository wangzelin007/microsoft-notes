# C:\Code\azure-cli\venv\Scripts
# mklink "C:\Code\wzl.ps1" "C:\Code\microsoft-notes\2021\powershell\wzl.ps1"
# mklink "D:\Code\wzl.ps1" "D:\Code\microsoft-notes\2021\powershell\wzl.ps1"

param(
 [Parameter(Mandatory=$True)]
 [string]
 $TYPE
)


if($TYPE -eq 'azcli'){
    azure-cli\env\Scripts\activate
    azdev setup --cli C:\code\azure-cli --repo C:\code\azure-cli-extensions
}
elseif($TYPE -eq 'azcli-ws'){
    azure-cli\env\Scripts\activate
    azdev setup --cli D:\code\azure-cli --repo D:\code\azure-cli-extensions
}
elseif($TYPE -eq 'extension'){
    azure-cli-extensions\env\Scripts\activate
}
elseif($TYPE -eq 'azdev'){
    azure-cli-dev-tools\env\Scripts\activate
    azdev setup --cli C:\code\azure-cli --repo C:\code\azure-cli-extensions
}
elseif($TYPE -eq 'azdev-ws'){
    azure-cli-dev-tools\env\Scripts\activate
    azdev setup --cli D:\code\azure-cli --repo D:\code\azure-cli-extensions
}