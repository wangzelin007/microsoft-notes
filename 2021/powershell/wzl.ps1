# C:\Code\azure-cli\venv\Scripts
#

param(
 [Parameter(Mandatory=$True)]
 [string]
 $TYPE
)

if($TYPE = 'azure-cli'){
    cd C:\Code\azure-cli\venv\Scripts
    .\activate
    azdev setup --cli C:\code\azure-cli --repo C:\code\azure-cli-extensions
}
elseif($TYPE = 'extension'){
    cd C:\Code\azure-cli-extensions\venv\Scripts
    .\activate
}
elseif($TYPE = 'dev'){
    cd C:\Code\azure-cli-dev-tools\venv\Scripts
    .\activate
}