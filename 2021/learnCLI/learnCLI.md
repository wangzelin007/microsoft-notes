什么是ignite？ 集中推广期
az rest: Invoke a custom request by http request.  
测试时都使用了装饰器： @ResourceGroupPreparer，会自动清理创建的资源。  
check 是怎么写出来的，意思就是我写这个check之前需要拿到一次请求的结果。
这个结果是通过调式断点的方式拿到的嘛？
还是保存在日志里？
还是别的什么方式？
# todo 
self.check('length(value)', 1)  
# todo 
self.check('length(value)', 4)  

patch方法用来更新局部资源
我们的 update 走哪个？
_begin_create_or_update -> put
_update_initial -> patch

g.generic_update_command('update', getter_name='get_vm_to_update', setter_name='update_vm', setter_type=compute_custom, command_type=compute_custom, supports_no_wait=True, validator=process_vm_update_namespace)
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
        PreviewItem
        ExperimentalItem
        # todo 区别
    getter_op_path
    setter_op_path
    custom_function_op_path
    GenericUpdateCommandOperation
    add_cli_command

# todo
vm 和 vmss
# todo 
vm_create_test_plan
# todo 
vmss_create_test_plan

aliases.json 用于mock

tempfile.mkstemp() 生成临时文件和目录，用户用完临时文件后需要自行将其删除。
返回值是元组：第一个元素是句柄，它是一个系统级句柄，指向一个打开的文件（等同于 os.open() 的返回值），第二元素是该文件的绝对路径。
_, public_settings = tempfile.mkstemp()
'C:\Users\ZELINW~1\AppData\Local\Temp\tmpkcaeo_8a'

@mock.patch('azure.cli.command_modules.vm.disk_encryption.set_vm', autospec=True)
If you set autospec=True then the mock will be created with a spec from the object being replaced. 
All attributes of the mock will also have the spec of the corresponding attribute of the object being replaced. 
Methods and functions being mocked will have their arguments checked and will raise a TypeError if they are called with the wrong signature.
@mock.patch('azure.cli.core.commands.client_factory.get_subscription_id', _mock_get_subscription_id)
patch() 接受一个已存在对象的全路径名，将其替换为一个新的值。 原来的值会在装饰器函数或上下文管理器完成后自动恢复回来。 默认情况下，所有值会被 MagicMock 实例替代。
可以通过给 patch() 提供第二个参数来将值替换成任何你想要的。

@unittest.skip('The identity is genereated dynamically. Template file should contain it')
@unittest.skip(reason)
Unconditionally skip the decorated test. reason should describe why the test is being skipped.

@live_only()
    return unittest.skipUnless(
        os.environ.get(ENV_LIVE_TEST, False),
        'This is a live only test. A live test will bypass all vcrpy components.')
@record_only()
    return unittest.skipUnless(
        not os.environ.get(ENV_LIVE_TEST, False),
        'This test is excluded from being run live. To force a recording, please remove the recording file.')

# todo
@StorageAccountPreparer(name_prefix='clitestbootdiag')
@api_version_constraint(ResourceType.MGMT_NETWORK, min_api='2017-08-01')
return unittest.skipUnless(get_support_api_version_func()(get_dummy_cli(), resource_type, **kwargs),
                               "Test not supported by current profile.")
@VirtualNetworkPreparer(location='eastus2euap', parameter_name='virtual_network')
az network vnet create/delete

# todo
@KeyVaultPreparer(name_prefix='vmlinuxkv', name_len=20, key='vault',
                      additional_params='--enabled-for-deployment true --enabled-for-template-deployment true')
az keyvault : Manage KeyVault keys, secrets, and certificates.

D:\code\azure-cli\src\azure-cli\azure\cli\command_modules\vm\custom.py :745
from azure.cli.command_modules.vm._template_builder import (build_vm_resource,
                                                                build_storage_account_resource, build_nic_resource,
                                                                build_vnet_resource, build_nsg_resource,
                                                                build_public_ip_resource, StorageProfile,
                                                                build_msi_role_assignment,
                                                                build_vm_linux_log_analytics_workspace_agent,
                                                                build_vm_windows_log_analytics_workspace_agent)

ARM Template: 
Azure Resource Manager templates are JavaScript Object Notation (JSON) files that define the infrastructure and configuration for your project.
https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/

ARM example: Support user_data for VM and VM Scale Sets
https://github.com/Azure/azure-cli/pull/18432
File changes:
src/azure-cli/azure/cli/command_modules/vm/_params.py
c.argument('user_data', help='UserData for the VM. It can be passed in as file or string.', completer=FilesCompleter(), type=file_type, min_api='2021-03-01')
c.argument('user_data', help='UserData for the virtual machines in the scale set. It can be passed in as file or string.', completer=FilesCompleter(), type=file_type, min_api='2021-03-01')
c.argument('user_data', help='UserData for the virtual machines in the scale set. It can be passed in as file or string. If empty string is passed in, the existing value will be deleted.', completer=FilesCompleter(), type=file_type, min_api='2021-03-01')
c.argument('user_data', help='UserData for the VM. It can be passed in as file or string. If empty string is passed in, the existing value will be deleted.', completer=FilesCompleter(), type=file_type, min_api='2021-03-01')

src/azure-cli/azure/cli/command_modules/vm/_template_builder.py
def build_vm_resource(user_data=None):
    if user_data:
        vm_properties['userData'] = b64encode(user_data)
    if user_data:
        vmss_properties['virtualMachineProfile']['userData'] = b64encode(user_data)

src/azure-cli/azure/cli/command_modules/vm/_validators.py
            namespace.vnet_name,
            namespace.user_data

src/azure-cli/azure/cli/command_modules/vm/custom.py
            data_disk_delete_option=None, user_data=None):
    if user_data:
        user_data = read_content_if_is_file(user_data)
    user_data=user_data)

def update_vm(user_data=None):
    if user_data is not None:
        from azure.cli.core.util import b64encode
        vm.user_data = b64encode(user_data)

src/azure-cli/azure/cli/command_modules/vm/tests/latest/recordings/test_vm_create_user_data.yaml
src/azure-cli/azure/cli/command_modules/vm/tests/latest/recordings/test_vmss_create_user_data.yaml

src/azure-cli/azure/cli/command_modules/vm/tests/latest/test_vm_commands.py
src/azure-cli/azure/cli/command_modules/vm/tests/latest/user_data.json