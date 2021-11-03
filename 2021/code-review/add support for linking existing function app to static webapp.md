[need-review](https://github.com/Azure/azure-cli/pull/20116)

src/azure-cli/azure/cli/command_modules/appservice/_validators.py +278
    functions = client.get_user_provided_function_apps_for_static_site(
        name=namespace.name, resource_group_name=namespace.resource_group_name)
    if list(functions):

src/azure-cli/azure/cli/command_modules/appservice/static_sites.py +431\
function_name = list(get_user_function(cmd, name, resource_group_name))[0].name


def get_user_functio():
    return client.get_user_provided_function_apps_for_static_site(name=name, resource_group_name=resource_group_name)
return: An iterator like instance of either StaticSiteUserProvidedFunctionAppsCollection or the result of cls(response)

------------------------------------
**mock**
def link_user_function:
    show_functionapp

@mock.patch("azure.cli.command_modules.appservice.static_sites.show_functionapp")  
def test_functions_link(self, *args, **kwargs):
    link_user_function(self.mock_cmd, self.name1, self.rg1, functionapp_resource_id)  
    self.staticapp_client.begin_register_user_provided_function_app_with_static_site.assert_called_once() -> (sdk)


def show_functionapp:
    get_user_function

@mock.patch("azure.cli.command_modules.appservice.static_sites.get_user_function", return_value=[mock.MagicMock()])
def test_functions_unlink(self, *args, **kwargs):
    unlink_user_function(self.mock_cmd, self.name1, self.rg1)
    self.staticapp_client.detach_user_provided_function_app_from_static_site.assert_called_once() -> (sdk)

np = mock.MagicMock() 自由构造mock对象