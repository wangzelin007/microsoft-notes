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
3. 初始化慢 存在
4. 1ES 优点, why?
5. 扩容
6. 价格对比

Email:
After test migration to 1ES pool, I have serveral questions to ask:
1. I noticed that three tasks are missing (如图片1所示), these tasks are atuo-injected when we use default pool.
我想确认他们丢失是否会造成什么影响。
2. 如图片2所示, task 1 使用的是 default pool, 其他task使用的是1ES pool, default pool 总是实时启动的。但是1ES pool 需要准备几分钟， 1ES pool 启动慢的问题有办法优化嘛？
3. 我们测试使用的是容量为20的池子，当我们想创建更大的池子时，产生了如图片3所示的报错，请问如何扩容 1ES pool。
4. default pool使用的时ADO pool, 请问 为什么现在推荐使用 1ES pool, 相比较 ADO pool 有哪些好处？
5. 使用1ES pool 和 ADO pool 所花费的费用谁更高？

After test migration to the 1ES pool, I have more questions to confirm:

1.	I noticed that three tasks are missing (as shown in picture1), these tasks are auto injected when we use the default pool. I would like to confirm whether their loss would take any effect?
2.	We create a 1ES pool with a capacity of 20. When we wanted to update a larger capacity, an error like the one shown in picture2 was raised. May I ask how to expand the 1ES pool? The increase quota work item has been in progress for more than a week.( https://mseng.visualstudio.com/Domino/_workitems/edit/1952951)
3.	Why is the 1ES pool recommended now, and what are the advantages compared to the default pool(ADO pool) ?
4.	Who is more expensive? the 1ES pool or the default pool(ADO pool), is there a comparison of the charges for the two types of pools?



2.	As shown in picture 2, task 1 uses the default pool, other tasks use the 1ES pool, and the default pool is always started in real-time. But the 1ES pool needs to be prepared for a few minutes. Is there any way to optimize the slow start of the 1ES pool?



start: 10:44
end: 

20台： 40*1.25*2=100 美元一天

50(6 Skipped 12 dependsOn)

ARM64：
Ubuntu 20.04 ARM64
Ubuntu Server 20.04 LTS ARM64
Windows 11 Enterprise - ARM64
Windows 11 Professional - ARM64