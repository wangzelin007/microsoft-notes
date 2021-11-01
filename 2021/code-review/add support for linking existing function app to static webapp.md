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
