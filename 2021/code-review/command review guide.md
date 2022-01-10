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

Title:
[App Config] BREAKING CHANGE: Support app service slots
[App Service] Fix #19550: `az staticwebapp users update`: Allow updating static web app user roles again 

Error:
MutuallyExclusiveArgumentError -相互排他性
InvalidArgumentValueError
ArgumentUsageError
RequiredArgumentMissingError - 明确的缺少参数

Test Exclude:
k8s-configuration: have E2E tests that we run in our fork that are not merged into upstream. 
k8s-extension: have E2E tests that we run in our fork that are not merged into upstream. 
spring-cloud: 
