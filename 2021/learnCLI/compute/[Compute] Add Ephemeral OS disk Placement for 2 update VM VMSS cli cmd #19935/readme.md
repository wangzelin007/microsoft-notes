https://github.com/Azure/azure-cli/issues/19935

Is your feature request related to a problem? Please describe.
we currently support Ephemeral os disks provisioning from the dedicated Cache disk space that comes with the VM size. So the customer is limited to using the max cache disk size space for provisioning the ephemeral OS disk. Due to increasing adaptation of Ephemeral OS disk and having a wide variety of VM Sizes without Cache disk space but having the temp disk space, we have implemented and started supporting the provisioning of Ephemeral OS disk from temp disk space also which will ensure customers can use the VM Sizes without Cache disk but with Temp disk space. Currently, VM Sizes which are having premium storage only support Cache disk, and also our popular lsv2 series does have a large temp disk but does not support Cache disk. so this feature can help in all these cases.
我们目前支持从 VM 大小附带的专用缓存磁盘空间配置临时操作系统磁盘。因此，客户只能使用最大缓存磁盘大小空间来配置临时 OS 磁盘。由于对 Ephemeral OS 磁盘的适配度越来越高，并且有各种各样的 VM Sizes，没有 Cache 磁盘空间但有临时磁盘空间，我们已经实施并开始支持从临时磁盘空间配置 Ephemeral OS 磁盘，这也将确保客户可以使用没有缓存磁盘但有临时磁盘空间的 VM 大小。目前，具有高级存储的 VM Sizes 仅支持 Cache 磁盘，而且我们流行的 lsv2 系列确实有一个大的临时磁盘，但不支持 Cache 磁盘。所以这个功能可以在所有这些情况下提供帮助。

Describe the solution you'd like
The previous PR #19751 covers the case for create VM/VMSS scenarios where Customer can specify the Ephemeral os disk placement when creating the vmss/vm .
Here This change exposes a new param customer can use to update the ephemeral os disk placement when updating the VM/ VMSS size to new one.
之前的 PR 19751 涵盖了创建 VMVMSS 场景的情况，其中客户可以在创建 vmssvm 时指定临时操作系统磁盘位置。此处此更改公开了一个新参数，客户可在将 VM VMSS 大小更新为新大小时使用该参数来更新临时操作系统磁盘位置。

Additional context
The cli cmds to be updated are az vm update, az vmss update

--------------------------------------------------------------
由于 CLI 还不支持 `--resize` 和 `--ephemeral-os-disk` 参数; 而且我们手头上还有一些 ignite 需求需要开发，所以无法在 ignite 之前上线这个需求。
同时我建议定一个会议先讨论一下如何实现 `--resize` 功能，因为这是 `--ephemeral-os-disk-placement` 的前置条件。
我们需要讨论如下事项：
1. resize 需要支持哪些选项。
2. 如何实现 resize 功能。 

Hi hari-bodicherla,
I am sorry to tell you that since CLI does not yet support the `--resize` argument and `--ephemeral-os-disk` argument in `az vm vmss update`, and we still have some ignite requirements to develop, so we cannot launch this requirement before ignite.
At the same time, I suggest discussing the `--resize` function first, because this is a precondition of `--ephemeral-os-disk-placement`.
I think we need to discuss the following matters:
1. What options need to be supported by `--resize`.
2. How to develop the `--resize` function.

Hi hari-bodicherla,
Since CLI does not yet support the `--ephemeral-os-disk` argument in `az vm resize`， do I need add both `--ephemeral-os-disk` argument and `--ephemeral-os-disk-placement` argument ?
And CLI does not have `az vmss resize` command, do you known which command I should modify in `az vmss` ?
May I ask you is this issue for ignite ?
Because we still have some ignite requirements to develop, so we cannot guarantee to launch this requirement before ignite.

-------------------------------------------------------------
[CacheDisk, ResourceDisk]
https://docs.microsoft.com/en-us/cli/azure/vm?view=azure-cli-latest#az_vm_update-examples
az vm update -n name -g group --set storageProfile.osDisk.diffDiskSettings.placement=CacheDisk
az vmss update --name MyScaleSet --resource-group MyResourceGroup --set virtualMachineProfile.storageProfile.osDisk.diffDiskSettings.placement=ResourceDisk

live
az vm update -n cli-test-vm-local-base -g cli_test_vm_create_ephemeral_os_disk_placementfcpgncm2ojewtqyb4xrjgaiod4ze7 --set storageProfile.osDisk.diffDiskSettings.placement=CacheDisk
(OperationNotAllowed) The 'Placement' option override for the ephemeral OS disk is not supported. Please upgrade the VM Size with desired placement option for provisioning the Ephemeral OS disk.
-------------------------------------------------------------

And I think before update or resize , you need to deallocate vm/vmss first, then update or resize and start vm/vmss in the end.

**代码逻辑**
az vm resize 
D:\code\azure-cli\src\azure-cli\azure\cli\command_modules\vm\commands.py
g.custom_command('resize', 'resize_vm', supports_no_wait=True)
D:\code\azure-cli\src\azure-cli\azure\cli\command_modules\vm\custom.py
def resize_vm(cmd, resource_group_name, vm_name, size, no_wait=False):
vm.storage_profile.osdisk.diffdisksettings.placement=placement **todo**

test_vm_create_state_modifications
self.cmd('vm deallocate --resource-group {rg} --name {vm}')
self._check_vm_power_state('PowerState/deallocated')
self.cmd('vm resize -g {rg} -n {vm} --size Standard_DS2_v2',
         checks=self.check('hardwareProfile.vmSize', 'Standard_DS2_v2'))

az vm update

az vmss update
