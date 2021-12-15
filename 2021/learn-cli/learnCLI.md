az rest: Invoke a custom request by http request.  

aliases.json 用于mock

check 值获取方式：
1. 断点调试
2. 直接执行对应的az命令  
check 说明：  
`self.check('length(value)', 1)` 一般用于确认创建了几个资源  

decorate 装饰器:  
`@ResourceGroupPreparer`，会自动清理创建的资源。
`@mock.patch('azure.cli.command_modules.vm.disk_encryption.set_vm', autospec=True)`  
If you set `autospec=True` then the mock will be created with a spec from the object being replaced.  
All attributes of the mock will also have the spec of the corresponding attribute of the object being replaced.  
Methods and functions being mocked will have their arguments checked and will raise a TypeError if they are called with the wrong signature.  
---------------
`@mock.patch('azure.cli.core.commands.client_factory.get_subscription_id', _mock_get_subscription_id)`
patch() 接受一个已存在对象的全路径名，将其替换为一个新的值。 原来的值会在装饰器函数或上下文管理器完成后自动恢复回来。默认情况下，所有值会被 MagicMock 实例替代。  
可以通过给 patch() 提供第二个参数来将值替换成任何你想要的。  
---------------
`@unittest.skip('The identity is genereated dynamically. Template file should contain it')`
`@unittest.skip(reason)`  
Unconditionally skip the decorated test. reason should describe why the test is being skipped.  
---------------
```
@live_only()
    return unittest.skipUnless(
        os.environ.get(ENV_LIVE_TEST, False),
        'This is a live only test. A live test will bypass all vcrpy components.')
@record_only()
    return unittest.skipUnless(
        not os.environ.get(ENV_LIVE_TEST, False),
        'This test is excluded from being run live. To force a recording, please remove the recording file.')
```
`@StorageAccountPreparer(name_prefix='clitestbootdiag')`  
存储相关，可以提供url测试  
```
@api_version_constraint(ResourceType.MGMT_NETWORK, min_api='2017-08-01')
return unittest.skipUnless(get_support_api_version_func()(get_dummy_cli(), resource_type, **kwargs),
                               "Test not supported by current profile.")
@VirtualNetworkPreparer(location='eastus2euap', parameter_name='virtual_network')
az network vnet create/delete
@KeyVaultPreparer(name_prefix='vmlinuxkv', name_len=20, key='vault',
                      additional_params='--enabled-for-deployment true --enabled-for-template-deployment true')
az keyvault : Manage KeyVault keys, secrets, and certificates.

generic_update_command:
generic_update_command('update', getter_name='get_vm_to_update', setter_name='update_vm', setter_type=compute_custom, command_type=compute_custom, supports_no_wait=True, validator=process_vm_update_namespace)
getter_name='get_vm_to_update' 先查询
setter_name='update_vm' 再更新
setter_type=compute_custom, 
command_type=compute_custom, 
supports_no_wait=True, 通过 wait 异步查询
validator=process_vm_update_namespace

generic_update_command
    _check_stale
    merged_kwargs
        _flatten_kwargs
            _merge_kwargs -> patch_kwargs
    merged_kwargs_custom
        _flatten_kwargs
    _apply_tags
        PreviewItem 就命令修改增加新属性
        ExperimentalItem 全新的不稳定功能
    getter_op_path
    setter_op_path
    custom_function_op_path
    GenericUpdateCommandOperation
    add_cli_command
```
ignite: 集中推广期

update：
_begin_create_or_update -> put  
_update_initial -> patch 方法用来更新局部资源  

vm && `vmss`：  
`vmss` vm scale set 管理一组vm的集合

`tempfile.mkstemp()` 生成临时文件和目录，用户用完临时文件后需要自行将其删除。   
返回值是元组：第一个元素是句柄，它是一个系统级句柄，指向一个打开的文件（等同于 os.open() 的返回值），第二元素是该文件的绝对路径。  
`_, public_settings = tempfile.mkstemp()
'C:\Users\ZELINW~1\AppData\Local\Temp\tmpkcaeo_8a'`

```python
# D:\code\azure-cli\src\azure-cli\azure\cli\command_modules\vm\custom.py :745
from azure.cli.command_modules.vm._template_builder import (build_vm_resource, build_storage_account_resource, build_nic_resource,
                                                            build_vnet_resource, build_nsg_resource,
                                                            build_public_ip_resource, StorageProfile,
                                                            build_msi_role_assignment,
                                                            build_vm_linux_log_analytics_workspace_agent,
                                                            build_vm_windows_log_analytics_workspace_agent)
```

ARM Template:   
Azure Resource Manager templates are JavaScript Object Notation (JSON) files that define the infrastructure and configuration for your project.  
https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/

PR example: 
Support user_data for VM and VM Scale Sets  
https://github.com/Azure/azure-cli/pull/18432  
My Issue: 
https://github.com/Azure/azure-cli/issues/19622
My change Files:  
```
src/azure-cli/azure/cli/command_modules/vm/_params.py
+    with self.argument_context('vm update', arg_group='Dedicated Host', min_api='2019-03-01') as c:
+        c.argument('dedicated_host_group', options_list=['--host-group'], is_preview=True, help="Name or ID of the dedicated host group that the VM will reside in. --host and --host-group can't be used together.")
+        c.argument('dedicated_host', options_list=['--host'], is_preview=True, help="ID of the dedicated host that the VM will reside in. --host and --host-group can't be used together.")

# src/azure-cli/azure/cli/command_modules/vm/_template_builder.py
src/azure-cli/azure/cli/command_modules/vm/_validators.py
    def process_vm_update_namespace(cmd, namespace):
+       _validate_vm_create_dedicated_host(cmd, namespace)

src/azure-cli/azure/cli/command_modules/vm/custom.py
def update_vm():
    +    # if dedicated_host is not None:
    +    #     vm.dedicated_host = dedicated_host
    +    #
    +    # if dedicated_host_group is not None:
    +    #     vm.dedicated_host_group = dedicated_host_group
src/azure-cli/azure/cli/command_modules/vm/tests/latest/test_vm_commands.py
+    def test_update_dedicated_host_e2e(self, resource_group, resource_group_location):
# src/azure-cli/azure/cli/command_modules/vm/tests/latest/user_data.json
# src/azure-cli/azure/cli/command_modules/vm/tests/latest/recordings/test_vm_create_user_data.yaml
# src/azure-cli/azure/cli/command_modules/vm/tests/latest/recordings/test_vmss_create_user_data.yaml
```

# 程序入口
1. `azure-cli\tools\automation\__main__.py` azdev
2. `azure-cli\src\azure-cli\azure\cli\__main__.py` az

# LROPoller
Use LROPoller for long running operation.