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
if not os_disk.diff_disk_settings.placement ?
az vm resize 
D:\code\azure-cli\src\azure-cli\azure\cli\command_modules\vm\commands.py
g.custom_command('resize', 'resize_vm', supports_no_wait=True)
D:\code\azure-cli\src\azure-cli\azure\cli\command_modules\vm\custom.py
def resize_vm(cmd, resource_group_name, vm_name, size, no_wait=False):
    vm = get_vm_to_update(cmd, resource_group_name, vm_name)
    vm.hardware_profile.vm_size == size
    vm.storage_profile.os_disk.diff_disk_settings.placement=ephemeral_os_disk_placement

**test**
test_vm_create_state_modifications
self.cmd('vm deallocate --resource-group {rg} --name {vm}')
self._check_vm_power_state('PowerState/deallocated')
self.cmd('vm resize -g {rg} -n {vm} --size Standard_DS2_v2',
         checks=self.check('hardwareProfile.vmSize', 'Standard_DS2_v2'))

az vm update
need to add --vm-sku in az vmss update and --size in az vm update first.
D:\code\azure-cli\src\azure-cli\azure\cli\command_modules\vm\commands.py
g.generic_update_command('update', getter_name='get_vm_to_update', setter_name='update_vm', setter_type=compute_custom, command_type=compute_custom, supports_no_wait=True, validator=process_vm_update_namespace)
D:\code\azure-cli\src\azure-cli\azure\cli\command_modules\vm\custom.py
def update_vm:
    if size is not None:
        vm.hardware_profile.vm_size = size
    vm.storage_profile.os_disk.diff_disk_settings.placement=ephemeral_os_disk_placement

az vmss update
need to add --vm-sku in az vmss update and --size in az vm update first.
**需要注意没有的时候怎么传**
D:\code\azure-cli\src\azure-cli\azure\cli\command_modules\vm\commands.py
g.generic_update_command('update', getter_name='get_vmss_modified', setter_name='update_vmss', supports_no_wait=True, command_type=compute_custom, validator=validate_vmss_update_namespace)
D:\code\azure-cli\src\azure-cli\azure\cli\command_modules\vm\custom.py
get_vmss_modified
    vmss = client.virtual_machine_scale_sets.get(resource_group_name, name)
update_vmss
    vmss = kwargs['parameters']
    if vm_sku is not None:
        vmss.sku.name = vm_sku
    vmss.virtual_machine_profile.storage_profile.os_disk.diff_disk_settings.placement=ephemeral_os_disk_placement
    return sdk_no_wait(no_wait, client.virtual_machine_scale_sets.begin_create_or_update,
                       resource_group_name, name, **kwargs)
**test**
azdev test test_vmss_update_ephemeral_os_disk_placement --live --discover

if not os_disk.diff_disk_settings.placement ?
if ephemeral_os_disk:
    info['os']['diffDiskSettings'] = {'option': 'Local'}
    # wzl add: caching = 'ReadWrite', because caching have a default value already, so just ignore.
    # local os disks require readonly caching, default to ReadOnly if os_disk_caching not specified.
    # if not os_disk_caching:
    #    os_disk_caching = 'ReadOnly'
    if ephemeral_os_disk_placement:
        info['os']['diffDiskSettings']['placement'] = ephemeral_os_disk_placement

**None**
diff_disk_settings=None

**Not None**
diff_disk_settings=(DiffDiskSettings){'additional_properties': {}, 'option': 'Local', 'placement': 'CacheDisk'}
DiffDiskSettings = cmd.get_models('DiffDiskSettings')
vm.host = DiffDiskSettings(option='Local', placement=ephemeral_os_disk_placement)

That make sense, but can we put this in next version?
And do you think CLI needs to support vmss resize too?
Maybe we can add both `az vm/vmss --resize --ephemeral-os-disk-placement ` in next version.
Because there is not enough time to test both `update` and `resize` before ignite.

**TODO**
1. examples N/A
2. validate --size and --sku-size D
3. help D
4. tests D
5. validate --ephemeral-os-disk D
6. validate --size --vm-sku not change Usage Error in --placement NOT NEED!
7. https://github.com/kevin1024/vcrpy/issues/533

**validate**
D:\code\azure-cli\src\azure-cli\azure\cli\command_modules\vm\commands.py
g.generic_update_command('update', getter_name='get_vm_to_update', setter_name='update_vm', setter_type=compute_custom, command_type=compute_custom, supports_no_wait=True, validator=process_vm_update_namespace)
g.generic_update_command('update', getter_name='get_vmss_modified', setter_name='update_vmss', supports_no_wait=True, command_type=compute_custom, validator=validate_vmss_update_namespace)

**error**
```
zure.core.exceptions.ResourceExistsError: (OperationNotAllowed) Operation'deallocate' is not supported for VMs or VM Scale Set instances using an ephemeral OS disk.
azure.core.exceptions.ResourceExistsError: (OperationNotAllowed) The 'Placement' option override for the ephemeral OS disk is not supported.Please upgrade the VM Size with desired placement option for provisioning the Ephemeral OS disk. Code: OperationNotAllowed
```
