```
az vm update -h
# az vm update --host -h
# az vm update --host-group -h
azdev test vm
azdev style vm
azdev linter vm
azdev test test_update_dedicated_host_e2e --live
git add
git commit
add host argument and host-group argument to az vm update
git push origin vm-update-support-dedicated-host-id
```
--------------------------------------------------------
**** Open a pull request ****
[Compute] az vm update: Add --host argument and --host-group argument to support assign an existing VM to a specific ADH

Description

[issue link](https://github.com/Azure/azure-cli/issues/19622)

Add --host argument to az vm update.
Add --host-group argument to az vm update.

Testing Guide

az vm deallocate -n {vm-name} -g {rg}

az vm update -n {vm-name} -g {rg} --host {host_id}  
or  
az vm update -n {vm-name} -g {rg} --host-group {host-group}')

az vm start -n {vm-name} -g {rg}')

---

This checklist is used to make sure that common guidelines for a pull request are followed.

- [ ] The PR title and description has followed the guideline in [Submitting Pull Requests](https://github.com/Azure/azure-cli/tree/dev/doc/authoring_command_modules#submitting-pull-requests).

- [ ] I adhere to the [Command Guidelines](https://github.com/Azure/azure-cli/blob/dev/doc/command_guidelines.md).

- [ ] I adhere to the [Error Handling Guidelines](https://github.com/Azure/azure-cli/blob/dev/doc/error_handling_guidelines.md).

--------------------------------------------------------
reviewer:
jsntcy
zhoxing-ms

Labels:
Compute - VM
--------------------------------------------------------
Squash and merge

--------------------------------------------------------
finish