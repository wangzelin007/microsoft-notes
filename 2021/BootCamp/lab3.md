D: Local Temporary Storage, will delete data when deallocated or moved

**VM and Disks**
- https://github.com/hansenms/azure_templates
- protection with premium storage

**VMSS and Availability Sets**
VMSS: 
1. Virtual Machine Scale Sets 可以动态扩缩容的vm集群。
2. vm 会被放置在不同的rack上。
3. 上限100台
4. Fault Domains: 
- isolate virtual machines for faults, default 2.
- protect me from unplanned downtime.
5. Update Domains: 
- isolate virtual machines for upgrades, default 5 max 20.
- protect me from planned downtime.
- domain 指把机器划分成几个区域。

**Availability zones**
- 99.99%
- mutiple data centers

**Region pairs**
- protection from disaster with data residency compliance
- esatUS vs westUS
- one region have mutiple data centers