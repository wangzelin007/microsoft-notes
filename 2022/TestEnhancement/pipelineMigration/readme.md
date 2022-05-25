Default agent pool:
https://dev.azure.com/azure-sdk/public/_apps/hub/ms.vss-ciworkflow.build-ci-hub?_a=edit-build-definition&id=1623&view=Tab_Tasks

vmImage: "windows-2019"
vmImage: 'ubuntu-20.04'
vmImage: 'macOS-10.15' continue to use the SDK Hosted Agents pool

East US 2

Azure Pipelines：
https://dev.azure.com/azure-sdk/internal/_settings/agentqueues?queueId=59&view=jobs

Hi @Scott,
When I create a 1ES Image, I cannot find a macOS-10.15 vm image.
Do you know how to get this image?

pool:
  name: 'Azure Pipelines'
  vmImage: 'macOS-10.15'

test migrate azure-pipelines-full-test.yml 10vm 时间？

  pool:
    name: 'azure-cli-pool-ubuntu-2004'
    vmImage: 'ubuntu-20.04'

  pool:
    name: 'azure-cli-pool-windows-2019'
    vmImage: 'windows-2019'

费用

1. missing tasks 
   Initialize CodeQL(auto-injected)
   Component Detection(auto-injected)
   Finalize CodeQL(auto-injected)
2. SBOM tasks 不影响
3. pipeline error ok
4. 初始化慢 存在

start: 10:44
end: 

20台： 40*1.25*2=100 美元一天

50(6 Skipped 12 dependsOn)

ARM64：
Ubuntu 20.04 ARM64
Ubuntu Server 20.04 LTS ARM64
Windows 11 Enterprise - ARM64
Windows 11 Professional - ARM64