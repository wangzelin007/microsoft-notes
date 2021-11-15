[PR link](https://github.com/Azure/azure-cli/pull/20043)

```
az vm update -h
az vm update --ephemeral-os-disk-placement -h
az vmss update -h
az vmss update --ephemeral-os-disk-placement -h
azdev test vm
azdev style vm
azdev linter vm
azdev test test_vm_update_ephemeral_os_disk_placement --live --discover
azdev test test_vmss_update_ephemeral_os_disk_placement --live --discover
git add
git commit
commit message
git push origin vm-vmss-update-support-ephemeral-os-disk-placement
```
--------------------------------------------------------
**** Open a pull request ****
[Compute] `az vm vmss update`: Add `--ephemeral-os-disk-placement` parameter to support choose the Ephemeral OS disk provisioning location

**Description**

[issue link](https://github.com/Azure/azure-cli/issues/19935)

Add --ephemeral-os-disk-placement argument to az vm update.
Add --ephemeral-os-disk-placement argument to az vmss update.

**Testing Guide**

az vm update -n MyVm -g MyResourceGroup --size {size} --ephemeral-os-disk-placement ResourceDisk
az vm update -n MyVm -g MyResourceGroup --size {size} --ephemeral-os-disk-placement CacheDisk
az vmss update -n MyVm -g MyResourceGroup --vm-sku {vm-sku} --ephemeral-os-disk-placement ResourceDisk
az vmss update -n MyVm -g MyResourceGroup --vm-sku {vm-sku} --ephemeral-os-disk-placement CacheDisk

**History Notes**

[Compute] `az vm update`: Add `--ephemeral-os-disk-placement` argument to support choose the Ephemeral OS disk provisioning location  
[Compute] `az vmss update`: Add `--ephemeral-os-disk-placement` argument to support choose the Ephemeral OS disk provisioning location

---

This checklist is used to make sure that common guidelines for a pull request are followed.

- [ ] The PR title and description has followed the guideline in [Submitting Pull Requests](https://github.com/Azure/azure-cli/tree/dev/doc/authoring_command_modules#submitting-pull-requests).

- [ ] I adhere to the [Command Guidelines](https://github.com/Azure/azure-cli/blob/dev/doc/command_guidelines.md).

- [ ] I adhere to the [Error Handling Guidelines](https://github.com/Azure/azure-cli/blob/dev/doc/error_handling_guidelines.md).

--------------------------------------------------------
reviewer:
jsntcy
zhoxing-ms
hari-bodicherla

Assignees:
wangzelin007
yonzhan

Labels:
Compute - VM
Compute - VMSS

Milestone
xxx

Create pull request

Linked issues

--------------------------------------------------------
Squash and merge

--------------------------------------------------------
finish


--------------------------------------------------------------------
for ci & for bump version
{compute} Bump disk 2021-04-01