```
az vm create -h
# az vm create --ephemeral-os-disk -h
# az vm create --ephemeral-os-disk-placement -h
# az vmss create --ephemeral-os-disk -h
# az vmss create --ephemeral-os-disk-placement -h
azdev test vm
azdev style vm
azdev linter vm
azdev test test_vm_create_ephemeral_os_disk --live
azdev test test_vm_create_ephemeral_os_disk_placement --live --discover
azdev test test_vmss_create_ephemeral_os_disk --live
azdev test test_vmss_create_ephemeral_os_disk_placement --live --discover
git add
git commit
add ephemeral_os_disk_placement argument to az vm vmss create
git push origin vm-update-support-dedicated-host-id
```
--------------------------------------------------------
**** Open a pull request ****
[Compute] `az vm vmss create`: Add `--ephemeral-os-disk-placement` argument for support to choose the Ephemeral OS disk provisioning location

**Description**

[issue link](https://github.com/Azure/azure-cli/issues/19751)

Add --ephemeral-os-disk-placement argument to az vm create.
Add --ephemeral-os-disk-placement argument to az vmss create.

**Testing Guide**

az vm create -n MyVm -g MyResourceGroup --image {image} --size Standard_DS4_v2 --location {loc} --ephemeral-os-disk --ephemeral-os-disk-placement ResourceDisk
az vm create -n MyVm -g MyResourceGroup --image {image} --location {loc} --ephemeral-os-disk --ephemeral-os-disk-placement CacheDisk
az vmss create -n MyVmss -g MyResourceGroup --image {image} --vm-sku Standard_DS4_v2 --ephemeral-os-disk --ephemeral-os-disk-placement ResourceDisk
az vmss create -n MyVmss -g MyResourceGroup --image {image} --ephemeral-os-disk --ephemeral-os-disk-placement CacheDisk 

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

Labels:
Compute - VM
Compute - VMSS
--------------------------------------------------------
Squash and merge

--------------------------------------------------------
finish