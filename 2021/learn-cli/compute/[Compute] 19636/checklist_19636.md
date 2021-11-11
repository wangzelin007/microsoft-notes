[PR link]()

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
add ephemeral_os_disk_placement argument to az vm vmss update
git push origin vm-vmss-update-support-ephemeral-os-disk-placement
```
--------------------------------------------------------
**** Open a pull request ****
[Compute] `az disk snapshot`: Add `--public-network-access` argument to control the policy for export on the disk

**Description**

[issue link](https://github.com/Azure/azure-cli/issues/19636)

- Customers can set, read and update PublicNetworkAccess, AcceleratedNetwork on Managed Disks and Snapshots.
- Customers can read CompletionPercent on Snapshots.

**Testing Guide**

az disk create --public-network-access Enabled --size-gb 5 -n {disk} -g {rg}
az disk update --public-network-access Disabled --size-gb 5 -n {disk} -g {rg}
az disk create --accelerated-network true --size-gb 5 -n {disk} -g {rg}
az disk create --accelerated-network false --size-gb 5 -n {disk} -g {rg}

az snapshot create --public-network-access Enabled --size-gb 5 -n {snapshot} -g {snapshot}
az snapshot update --public-network-access Disabled --size-gb 5 -n {snapshot} -g {snapshot}
az snapshot create --accelerated-network true --size-gb 5 -n {snapshot} -g {snapshot}
az snapshot update --accelerated-network false --size-gb 5 -n {snapshot} -g {snapshot}

**History Notes**

[Compute] `az disk create`: Add `--public-network-access` argument to control the policy for export on the disk
[Compute] `az disk update`: Add `--public-network-access` argument to control the policy for export on the disk
[Compute] `az disk create`: Add `--accelerated-network` argument to support the accelerated networking
[Compute] `az disk update`: Add `--accelerated-network` argument to support the accelerated networking
[Compute] `az snapshot create`: Add `--public-network-access` argument to control the policy for export on the disk
[Compute] `az snapshot update`: Add `--public-network-access` argument to control the policy for export on the disk
[Compute] `az snapshot create`: Add `--accelerated-network` argument support the accelerated networking
[Compute] `az snapshot update`: Add `--accelerated-network` argument support the accelerated networking
[Compute] `az snapshot show`: support to display the completion percent for the background copy when a resource is created via the `--copy-start` operation

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