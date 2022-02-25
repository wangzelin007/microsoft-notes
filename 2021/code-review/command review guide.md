Common:
- Do we need to consider adding confirmation=True for the delete operation ?
- Filpath to File path
- May I ask is this the tag stored in ARM service? If so, do we need to consider using **tags_type**?
- Do we need these two methods? If not, please delete them
- vm_properties['additionalCapabilities'] = {'ultraSSDEnabled': ultra_ssd_enabled} -> vm_properties['additionalCapabilities']['ultraSSDEnabled'] = ultra_ssd_enabled
- 'hibernation_enabled' to 'enable_hibernation'
- I want to confirm with you that container.name and container_name are not None at any time, right?
- Could you pull the latest code from remote main branch first, and then fix the CI style check issue below. After that, we will help you solve the remaining CI issue later.
- Will the change of parameter type cause breaking change to users?
- May I ask you to add some scenario tests for those new commands?
- Could you please use a specific error type instead of CLIError?
- Could you please address those conflicts?
- Could we abstract it into CLIArgumentType, so that we don't have to define the same flags repeatedly
- Please use the first person voice
- It seems that it and connectedvmware vm extension create have several common parameters. Could we consider using for loop to share them? (scope)
- May I ask will backup_config_response.properties always have property storage_type or cross_region_restore_flag
- use dict.get(key[, default=None]) to assign default values.
- May I ask could we get those enumeration values from the Python SDK?
- Please add more context for why this is changed.
- [] means this change is customer-facing and the message will be put into HISTORY.rst.
  {} means this change is not customer-facing and the message will NOT be included in HISTORY.rst.
  Usually bump version is not customer-facing.
  May I ask whether description 2-4 is customer-facing?
  If we have multiple customer-facing changes, we need add them in the History Notes one by one, so we can automatically generate release note from History Notes instead of PR title.
- The failure of CI is caused by the api-version of ResourceType.MGMT_CONTAINERREGISTRY upgraded from 2021-06-01-preview to 2021-08-01-preview and needed to re record these tests in live mode
- type=str is the default setting, so we don't need an explicit declaration

Azure-cli-extensions:
- (By the way) If you want to release the new extension version, please write the description of changes into HISTORY.rst and update setup.py.
- src/service_name.json when a new extension is added.

Azure-cli:
- Could we get the valid value of build_pool_size from Python SDK?
- Since @ResourceGroupPreparer is used in this test, the snapshot will be automatically removed after this test is completed.
Therefore, the exposure of SAS token will not cause security vulnerabilities. We can consider adding exclusion for credential scanning in file CredScanSuppressions.json
- Sorry, because the comments were resolved a little late, and included upgrading api-version, this poses a risk to the quality of CLI and may blocking CLI release.
Therefore, this PR cannot catch up with the release of this sprint. Next time, please try to get the PR ready on the code completion date. The release time of the next sprint is 2022-02-08 (this is also the milestone we set at the beginning for this PR)

Title:
[App Config] BREAKING CHANGE: Support app service slots
[App Service] Fix #19550: `az staticwebapp users update`: Allow updating static web app user roles again 

Error:
MutuallyExclusiveArgumentError -相互排他性
InvalidArgumentValueError
ArgumentUsageError
ValidationError
RequiredArgumentMissingError - 明确的缺少参数

Test Exclude:
k8s-configuration: have E2E tests that we run in our fork that are not merged into upstream. 
k8s-extension: have E2E tests that we run in our fork that are not merged into upstream. 
spring-cloud: 

ERROR:
1. 修改代码也能导致大量重录 [jepio](https://github.com/Azure/azure-cli/pull/21028)

------
切换profile:
az cloud update --profile 2020-09-01-hybrid
重新录制： re-record
get all failed test case in profile 2018-03-01-hybrid 
`azdev test vm --repo=./ --src=HEAD --tgt=origin/dev --no-exitfirst --profile 2018-03-01-hybrid --verbose --series`
re-run error cases to generate recording files:
`azdev test vm --no-exitfirst --live --lf --profile 2018-03-01-hybrid`
{
  "status": "Failed",
  "error": {
    "code": "DeploymentFailed",
    "message": "At least one resource deployment operation failed. Please list deployment operations for details. Please see https://aka.ms/DeployOperations for usage details.",
    "details": [
      {
        "code": "BadRequest",
        "message": {
          "error": {
            "details": [
              {
                "message": "Could not find member vmSizeProperties on object of type VMHardwareProfile. Path properties.hardwareProfile.vmSizeProperties, line 1, position 110.",
                "target": "vm.properties.hardwareProfile.vmSizeProperties"
              },
              {
                "message": "Could not find member additionalCapabilities on object of type Properties. Path properties.additionalCapabilities, line 1, position 1230.",
                "target": "vm.properties.additionalCapabilities"
              }
            ],
            "code": "BadRequest",
            "message": "The request message is invalid."
          }
        }
      }
    ]
  }
}

get all failed test case in profile 2019-03-01-hybrid
`azdev test vm --repo=./ --src=HEAD --tgt=origin/dev --no-exitfirst --profile 2019-03-01-hybrid --verbose --series`
re-run error cases to generate recording files:
`azdev test vm --no-exitfirst --live --lf --profile 2019-03-01-hybrid`


get all failed test case in profile 2020-09-01-hybrid
`azdev test vm --repo=./ --src=HEAD --tgt=origin/dev --no-exitfirst --profile 2020-09-01-hybrid --verbose --series`
re-run error cases to generate recording files:
`azdev test vm --no-exitfirst --live --lf --profile 2020-09-01-hybrid`

get all failed test case in profile latest
`azdev test vm --repo=./ --src=HEAD --tgt=origin/dev --no-exitfirst --profile latest --verbose --series`
re-run error cases to generate recording files:
`azdev test vm --no-exitfirst --live --lf --profile latest`

明细测试：
azdev test test_vm_secret_e2e_test --debug --profile 2018-03-01-hybrid
azdev test test_vm_secret_e2e_test --debug --profile 2019-03-01-hybrid
[x] azdev test test_vm_secret_e2e_test --debug --profile 2020-09-01-hybrid
azdev test test_vm_secret_e2e_test --debug --profile latest

live测试：
azdev test test_vm_secret_e2e_test --live --profile 2018-03-01-hybrid
azdev test test_vm_secret_e2e_test --live --profile 2019-03-01-hybrid
[x] azdev test test_vm_secret_e2e_test --live --profile 2020-09-01-hybrid
azdev test test_vm_secret_e2e_test --live --profile latest

2018-03-01-hybrid: 5
test_custom_image azure.cli.core.azclierror.DeploymentError
test_vm_create_by_attach_os_and_data_disks azure.cli.core.azclierror.DeploymentError
test_vm_create_ubuntu azure.cli.core.azclierror.DeploymentError
test_vmss_create_options azure.cli.core.azclierror.DeploymentError
test_set_os_disk_size azure.common.AzureHttpError:
azdev test test_vm_create_ubuntu --debug --profile 2018-03-01-hybrid
az vm create --resource-group zelin62 --admin-username ubuntu --name cli-test-vm2 --authentication-type ssh --image UbuntuLTS --ssh-key-value 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCbIg1guRHbI0lV11wWDt1r2cUdcNd27CJsg+SfgC7miZeubtwUhbsPdhMQsfDyhOWHq1+ZL0M+nJZV63d/1dhmhtgyOqejUwrPlzKhydsbrsdUor+JmNJDdW01v7BXHyuymT8G4s09jCasNOwiufbP/qp72ruu0bIA1nySsvlf9pCQAuFkAnVnf/rFhUlOkhtRpwcq8SUNY2zRHR/EKb/4NWY1JzR4sa3q2fWIJdrrX0DvLoa5g9bIEd4Df79ba7v+yiUBOS0zT2ll+z4g9izHK3EO5d8hL4jYxcjKs+wcslSYRWrascfscLgMlMGh0CdKeNTDjHpGPncaf3Z+FwwwjWeuiNBxv7bJo13/8B/098KlVDl4GZqsoBCEjPyJfV6hO0y/LkRGkk7oHWKgeWAfKtfLItRp00eZ4fcJNK9kCaSMmEugoZWcI7NGbZXzqFWqbpRI7NcDP9+WIQ+i9U5vqWsqd/zng4kbuAJ6UuKqIzB0upYrLShfQE3SAck8oaLhJqqq56VfDuASNpJKidV+zq27HfSBmbXnkR/5AK337dc3MXKJypoK/QPMLKUAP5XLPbs+NddJQV7EZXd29DLgp+fRIg3edpKdO7ZErWhv7d+3Kws+e1Y+ypmR2WIVSwVyBEUfgv2C8Ts9gnTF4pNcEY/S2aBicz5Ew2+jdyGNQQ== test@example.com\n' --location westus --data-disk-sizes-gb 1 --data-disk-caching ReadOnly


2019-03-01-hybrid: 10
test_vm_custom_image  azure.cli.core.azclierror.DeploymentError
test_vm_create_by_attach_os_and_data_disks  azure.cli.core.azclierror.DeploymentError
test_vm_generic_update  azure.cli.core.azclierror.DeploymentError
test_vm_create_ubuntu  azure.cli.core.azclierror.DeploymentError
test_vmss_create_options  azure.cli.core.azclierror.DeploymentError
test_vm_create_zones  azure.cli.core.azclierror.InvalidTemplateError
test_vmss_create_single_zone azure.cli.core.azclierror.InvalidTemplateError
test_vmss_create_x_zones azure.cli.core.azclierror.InvalidTemplateError
test_vmss_create_zonal_with_fd azure.cli.core.azclierror.InvalidTemplateError
test_vm_set_os_disk_size azure.common.AzureHttpError:

2020-09-01-hybrid: 5
test_vm_create_by_attach_os_and_data_disks azure.cli.core.azclierror.DeploymentError
test_vm_create_ubuntu azure.cli.core.azclierror.DeploymentError
test_vmss_create_options azure.cli.core.azclierror.DeploymentError
test_vm_generic_update azure.cli.core.azclierror.DeploymentError
test_vm_custom_image azure.core.exceptions.HttpResponseError
azdev test test_vmss_create_and_modify --profile 2020-09-01-hybrid --live done

latest: 26
VMCreateAndStateModificationsScenarioTest::test_vm_create_state_modifications - SystemExit: 2
VMCreateAndStateModificationsScenarioTest::test_vm_user_update_win - SystemExit: 2
VMMonitorTestDefault::test_vm_create_with_monitor - SystemExit: 2
VMMonitorTestCreateWindows::test_vm_create_with_workspace_windows - SystemExit: 2
VMMonitorTestUpdateLinux::test_vm_update_with_workspace_linux - SystemExit: 2
VMCreateExistingOptions::test_vm_create_existing_options - SystemExit: 2
VMCreateExistingOptions::test_vm_create_provision_vm_agent - SystemExit: 2
VMCreateExistingIdsOptions::test_vm_create_existing_ids_options - SystemExit: 2
VMDiskAttachDetachTest::test_vm_ultra_ssd_storage_sku - azure.core.exceptions.HttpResponseError: (LocationNotSupportAvaila
VMDiskAttachDetachTest::test_vm_vmss_update_ultra_ssd_enabled - azure.cli.core.azclierror.InvalidTemplateError: {"error":{
VMSSCreateOptions::test_vmss_create_options - SystemExit: 2
VMSSCreateBalancerOptionsTest::test_vmss_create_default_app_gateway - azure.cli.core.azclierror.InvalidTemplateError: {"er
AcceleratedNetworkingTest::test_vmss_accelerated_networking - SystemExit: 2
VMSSCreateExistingOptions::test_vmss_create_existing_options - SystemExit: 2
VMSSCreateExistingIdsOptions::test_vmss_create_existing_ids_options - SystemExit: 2
MSIScenarioTest::test_vm_msi - azure.cli.core.azclierror.DeploymentError: {"status":"Failed","error":{"code":"DeploymentFa
MSIScenarioTest::test_vmss_msi - azure.cli.core.azclierror.DeploymentError: {"status":"Failed","error":{"code":"Deployment
VMZoneScenarioTest::test_vm_create_zones - azure.cli.core.azclierror.InvalidTemplateError: {"error":{"code":"InvalidTempla
VMDiskEncryptionTest::test_vmss_disk_encryption_e2e - SystemExit: 2
VMGalleryImage::test_create_vm_with_shared_gallery_image - azure.core.exceptions.ResourceNotFoundError: (NotFound) The ent
VMGalleryImage::test_gallery_e2e - azure.core.exceptions.HttpResponseError: (InvalidParameter) Gallery image version publi
VMGalleryImage::test_shared_gallery - azure.core.exceptions.HttpResponseError: (InvalidParameter) Cannot update the galler
DiskEncryptionSetTest::test_disk_encryption_set - azure.core.exceptions.ResourceExistsError: (KeyVaultAndDiskInDifferentRe
VMCreateAutoCreateSubnetScenarioTest::test_vm_create_auto_create_subnet - knack.util.CLIError: Can't overwrite existing ca
VMSSOrchestrationModeScenarioTest::test_vmss_complex_orchestration_mode - azure.cli.core.azclierror.DeploymentError: {"sta
DiskZRSScenarioTest::test_disk_zrs - azure.core.exceptions.HttpResponseError: (InvalidParameter) SKU StandardSSD_ZRS is no

azdev test test_update_dedicated_host_e2e --profile latest --live done
quota:
Standard DSv3 Family vCPUs: Microsoft.Compute: East US 2: 1000
**rg name 最好保持唯一！**
azdev test test_vm_error_on_zone_unavailable --profile latest --live done
azdev test test_vmss_windows_patch_mode --profile latest --live done

T: azdev test test_vm_create_ubuntu --profile latest --live
F: azdev test test_vm_create_ubuntu --profile 2018-03-01-hybrid --live

TODO:
E       azure.cli.core.azclierror.DeploymentError: {"status":"Failed","error":{"code":"DeploymentFailed","message":"At least one resource deployment operation failed. Please list deployment operations for details. Please see https://aka.ms/DeployOperations for usage details.","details":[{"code":"BadRequest","message":"{\r\n  \"error\": {\r\n    \"code\": \"BadRequest\",\r\n    \"message\": \"Could not find member 'deleteOption' on object of type 'DataDisk'. Path 'properties.storageProfile.dataDisks[0].deleteOption', line 1, position 736.\",\r\n    \"target\": \"vm.properties.storageProfile.dataDisks[0].deleteOption\"\r\n  }\r\n}"}]}}
