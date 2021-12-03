ls env:
import os
os.environ['AZURE_CLI_TEST_COMMAND_COVERAGE']="True"

import os path=r"E:\env" command =r"setx WORK1 %s /m"%path os.system(command)

[environment]::GetEnvironmentvariable("AZURE_CLI_TEST_COMMAND_COVERAGE", "User")
[environment]::GetEnvironmentvariable("azure_client_secret", "User")

[environment]::SetEnvironmentvariable("变量名称", "变量值", "User")
[environment]::SetEnvironmentvariable("AZURE_CLI_TEST_COMMAND_COVERAGE", "True", "User")
