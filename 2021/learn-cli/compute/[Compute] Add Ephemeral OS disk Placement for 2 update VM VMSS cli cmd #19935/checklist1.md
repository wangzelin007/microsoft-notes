[PR link](https://github.com/Azure/azure-cli/pull/20043)

```
az vm update -h
az vm update --size -h
az vmss update -h
az vmss update --vm-sku -h
azdev test vm
azdev style vm
azdev linter vm
azdev test test_vm_update_size --live --discover
azdev test test_vmss_update_vm_sku --live --discover
git add
git commit
add size vm-sku argument to az vm vmss update
git push origin vm-vmss-update-support-size-vmsku
```
--------------------------------------------------------
**** Open a pull request ****
[Compute] `az vm vmss update`: Add `--size` parameter `--vm-sku` argument to support the resize

**Description**

[issue link](https://github.com/Azure/azure-cli/issues/19970)

Add --size argument to az vm update.
Add --vm-sku argument to az vmss update.

**Testing Guide**

az vm update -n MyVm -g MyResourceGroup --size {size}
az vmss update -n MyVm -g MyResourceGroup --vm-sku {vm-sku}

**History Notes**

[Compute] `az vm update`: Add `--size` argument to support the resize  
[Compute] `az vmss update`: Add `--vm-sku` argument to support the resize

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

Milestone

--------------------------------------------------------
Squash and merge

--------------------------------------------------------
finish