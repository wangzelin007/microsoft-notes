1. python -m venv env --prompt xxx
2. pip install azdev
3. azdev setup --cli D:\code\azure-cli --repo D:\code\azure-cli-extensions
4. azdev setup --cli C:\code\azure-cli --repo C:\code\azure-cli-extensions
5. pip install nose
6. az login
7. az account show

[comment]: <> (2. .\20211026\Scripts\activate)
[comment]: <> (3. copy C:\Users\zelinwang\Anaconda3\envs\xxx\python.exe to C:\Users\zelinwang\Anaconda3\envs\xxx\Scripts 暂时不支持py3.10)
[comment]: <> (7. rm pywin32_system32 && pywin32-302.dist-info)
[comment]: <> (8. pip install pywin32==228)

推荐Windows Terminal + PowerShell 7+

**problem**
```
log:
subprocess.CalledProcessError: Command '['C:\\Users\\zelinwang\\Anaconda3\\envs\\azure-msal\\Scripts\\python', '-m', 'pip', 'install', '--upgrade', 'pip']' returned non-zero exit status 1
fix:
copy C:\Users\zelinwang\Anaconda3\envs\azure-msal\python.exe to C:\Users\zelinwang\Anaconda3\envs\azure-msal\Scripts

# cli 代码不是最新的
vcr.errors.CannotOverwriteExistingCassetteException: Can't overwrite existing cassette ('/home/vsts/work/1/s/src/azure-cli/azure/cli/command_modules/vm/tests/latest/recordings/test_vmss_create_ephemeral_os_disk_placement.yaml') in your current record mode ('once').

# login 失败
azdev setup --cli D:\code\azure-cli --repo D:\code\azure-cli-extensions --debug

az account show
az account set -s 0b1f6471-1bf0-4dda-aec3-cb9272f09590

No match for the request (<Request (GET) https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/cli_test_vmss_create_ephemeral_os_disk_placement000001/providers/Microsoft.Compute/virtualMachineScaleSets/cli-test-vmss-local-base?api-version=2021-07-01>) was found.
resetup && recheckout from dev

ImportError: DLL load failed while importing _ssl: 找不到指定的模块。
windows 查看环境变量:
TODO 

TypeError: request() got an unexpected keyword argument 'error_template'
Unknown

ImportError: DLL load failed while importing win32file
delete:
C:\Users\zelinwang\Anaconda3\envs\azure-20211026\Lib\site-packages
pywin32_system32
pywin32-302.dist-info
pip install pywin32==228

replace azdev package
https://github.com/StrawnSC/azure-cli-dev-tools.git

AttributeError: module 'azure.mgmt.cosmosdb.operations' has no attribute 'LocationsOperations'
直接在 azure-cli 中搜索 azure-mgmt-cosmosdb 版本

ImportError: DLL load failed while importing _ctypes: 找不到指定的模块。

```

**install venv in D:\code\azure-cli\venv TODO**