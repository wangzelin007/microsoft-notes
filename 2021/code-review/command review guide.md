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
- Could we use `deprecate_info=c.deprecate(target='xxx', redirect='xxx', hide=True)` [deprecating-commands-and-arguments](https://github.com/Azure/azure-cli/blob/dev/doc/authoring_command_modules/authoring_commands.md#deprecating-commands-and-arguments) to hide these original commands and give users a few months to migrate their usage to new commands?
  Otherwise, deleting these original commands now may cause a sudden breaking change to the users.


Azure-cli-extensions:
- (By the way) If you want to release the new extension version, please write the description of changes into HISTORY.rst and update setup.py.
- src/service_name.json when a new extension is added.

Azure-cli:
- Could we get the valid value of build_pool_size from Python SDK?
- Since @ResourceGroupPreparer is used in this test, the snapshot will be automatically removed after this test is completed.
Therefore, the exposure of SAS token will not cause security vulnerabilities. We can consider adding exclusion for credential scanning in file CredScanSuppressions.json
- Sorry, because the comments were resolved a little late, and included upgrading api-version, this poses a risk to the quality of CLI and may blocking CLI release.
Therefore, this PR cannot catch up with the release of this sprint. Next time, please try to get the PR ready on the code completion date. The release time of the next sprint is 2022-02-08 (this is also the milestone we set at the beginning for this PR)

Please make sure to get this pr ready to merge before 2022/05/20.
Otherwise, this PR cannot catch up with the release of this sprint.
And the release time of the next sprint is 2022/07/05.

Could you take it as high priority since currently Azure CLI release is blocked by this issue and we need to ship it tomorrow. Thanks a lot.

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
**不要同时 download 多个 azcli**  
**reset: 删除 C:\Users\zelinwang\[.azdev,.azure] 等目录**  
**不要同时运行多个profile**

------
切换profile:
az cloud update --profile 2020-09-01-hybrid
重新录制： re-record
get all failed test case in profile 2018-03-01-hybrid 
`azdev test vm --repo=./ --src=HEAD --tgt=origin/dev --no-exitfirst --profile 2018-03-01-hybrid --verbose --series`
re-run error cases to generate recording files:
`azdev test vm --no-exitfirst --live --lf --profile 2018-03-01-hybrid`

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

github filter:
review-requested:wangzelin007
CLI:
is:open is:pr draft:false -label:do-not-merge -label:"Do Not Merge" milestone:"May 2022 (2022-05-24) - For Build" created:>2022-01-01
Extensions:
is:open is:pr draft:false -label:do-not-merge -label:"Do Not Merge" milestone:"May 2022 (2022-05-24)" created:>2022-01-01
Xing:

sprint:
is:open is:pr draft:false -label:do-not-merge -label:"Do Not Merge" milestone:"May 2022 (2022-05-24) - For Build" created:>2022-01-01 