The document provides instructions and guidelines on how to author individual commands.
该文档提供了有关如何编写单个命令的说明和指南

**AUTHORING COMMANDS**

[1. Write the Command Loader](#write-the-command-loader)

[2. Write a Command](#write-a-command)

[3. Register Commands](#register-commands)

[4. Write Help Entry](#write-help-entry) 编写帮助条目

[5. Customize Arguments](#customize-arguments) 自定义参数

**ADDITIONAL TOPICS**

[6. Keyword Argument (kwarg) Reference](#keyword-argument-reference) 关键字参数参考

[7. Supporting the IDs Parameter](#supporting-the-ids-parameter)

[8. Supporting Name or ID Parameters](#supporting-name-or-id-parameters)

[9. Generic Update Commands](#generic-update-commands) 通用更新命令

[10. Custom Table Formats](#custom-table-formats) 自定义表格格式

[11. Tab Completion (bash only)](#tab-completion) Command-line completion 自动补全

[12. Validators](#validators) 验证器

[13. Registering Flag Arguments](#registering-flags) 注册标志参数

[14. Registering Enum Arguments](#registering-enums) 注册枚举参数

[15. Preventing particular extensions from being loading](#extension-suppression) 预防加载特定扩展

[16. Deprecating Commands and Arguments](#deprecating-commands-and-arguments) 弃用命令和参数

[17. Multi-API Aware Modules](#multi-api-aware-modules) 多API感知模块

[18. Preview Commands and Arguments](#preview-commands-and-arguments) 预览命令和参数

Authoring Commands
=============================

## Write the Command Loader

As of version 2.0.24, Azure CLI is based on the Knack framework (https://github.com/Microsoft/knack), which uses the `CLICommandsLoader` class as the mechanism 机制 for loading a module. In Azure CLI, you will create your own loader which will inherit 继承 from the `AzCommandsLoader` class.  The basic structure is:

```Python
class MyCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.sdk.util import CliCommandType
        from azure.cli.core.profiles._shared import MGMT_MYTYPE
        mymod_custom = CliCommandType(operations_tmpl='azure.cli.command_modules.mymod.custom#{}')

        super(MyCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                               resource_type=MGMT_MYTYPE,
                                               custom_command_type=mymod_custom)

    def load_command_table(self, args):
        # TODO: Register command groups and commands here
        return self.command_table

    def load_arguments(self, command):
        # TODO: Register argument contexts and arguments here

COMMAND_LOADER_CLS = MyCommandsLoader
```

Note that `MGMT_MYTYPE` will need to be added to the `azure\cli\core\profiles\_shared.py` file. See [Multi-API Aware Modules](#multi-api-aware-modules)

```Python
class ResourceType(Enum):  # pylint: disable=too-few-public-methods
    ...
    MGMT_MYTYPE = ('azure.mgmt.mytype', 'MyTypeManagementClient')
    ...
```

## Write a Command

Write your command as a simple function, specifying your arguments as the parameter names.

***Parameter Naming Guidance***

When choosing names, it is recommended that you look at similar commands and follow those naming conventions to take advantage of any aliasing that may already be in place. For example, you should choose `resource_group_name` over `rg`, `resource_group` or some other shorthand, because this parameter is globally aliased and you will inherit the `-g` short option and the completer.
选择名称时，建议您查看类似的命令并遵循这些命名约定以利用可能已经存在的任何别名。
例如，你应该选择 `resource_group_name` 而不是 `rg`、`resource_group` 或其他一些简写，因为这个参数是全局别名的，你将继承 `-g` 短选项和完成者。


Avoid using a parameter name called `name` as this is a very common alias in the CLI and will often create aliasing conflicts.

If you specify a default value in your function signature, this will flag the argument as optional and will automatically display the default value in the help text for the command. Any parameters that do not have a default value are required and will automatically appear in help with the [Required] label. The required and default behaviors for arguments can be overridden (see Argument Customization below) but this is not generally needed.
如果在函数签名中指定默认值，这会将参数标记为可选，并将自动在命令的帮助文本中显示默认值。
任何没有默认值的参数都是必需的，并且会自动出现在带有 [Required] 标签的帮助中。可以覆盖参数的必需和默认行为（请参阅下面的参数自定义），但这通常不是必需的。


***Special Arguments***

There are two arguments you may include in your custom command that are reserved by the infrastructure and have special meaning.
您可以在自定义命令中包含两个参数，它们由基础架构保留并具有特殊含义。

`cmd`: If used, this should be the first argument in your custom command, and allows you to access the command instance within your custom command. This will allow you to access the CLI context and numerous helper methods to make writing your command simpler, particularly when working with a multi-API style module.
如果使用，这应该是自定义命令中的第一个参数，并允许您访问自定义命令中的命令实例。这将允许您访问 CLI 上下文和众多帮助程序方法，使您的命令编写更简单，尤其是在使用多 API 样式模块时。

`client`: If your command has registered the `client_factory` keyword argument, that factory will be passed into this variable. It can appear anywhere in your command signature.
如果您的命令注册了 `client_factory` 关键字参数，则该工厂将被传递到此变量中。它可以出现在您的命令签名中的任何位置。

## Register Commands

Before your command can be used in the CLI, it must be registered. Within the `load_command_table` method of your command loader, you will have something like:

```Python
# (1) Registering a command type for reuse among groups
mymod_sdk = CliCommandType(
    operations_tmpl='azure.mgmt.mymod.operations#MyOperations.{}',
    client_factory=cf_mymod
)

# (2) Registering a command group
with self.command_group('mymod', mymod_sdk) as g:
    # (3) Registering different types of commands
    g.command('command1', 'do_something_1')
    g.custom_command('command2', 'do_something_2')
    g.generic_update_command('update', custom_function_name='my_custom_update')
    g.wait_command('wait')
    g.show_command('show')
```

At this point, you should be able to access your command using `az [name]` and access the built-in help with `az [name] -h/--help`. Your command will automatically be 'wired up' with the global parameters.  See below for amplifying information.
此时，您应该能够使用 `az [name]` 访问您的命令，并使用 `az [name] -h--help` 访问内置帮助。您的命令将自动与全局参数“连接”。有关放大信息，请参见下文。

**(1) CliCommandType**

CliCommandType is a way to group and reuse and keyword arguments supported by commands. Earlier, in the `__init__` method of the `MyCommandsLoader` class, we created a `mymod_custom` variable and assigned it to the `custom_command_type` keyword argument. This will be used any time you use the `custom_command` method within a command group. It is registered with the loader since most modules typically put all of their custom methods in a single file.
CliCommandType 是一种对命令支持的关键字参数进行分组和重用的方法。之前，在`MyCommandsLoader` 类的`__init__` 方法中，我们创建了一个`mymod_custom` 变量并将其分配给`custom_command_type` 关键字参数。这将在您在命令组中使用 `custom_command` 方法时使用。它在加载器中注册，因为大多数模块通常将所有自定义方法放在一个文件中。

**(2) Command Group Helper**

```Python
command_group(self, group_name, command_type=None, **kwargs)
```
- `group_name`: the group name ('network', 'storage account', etc.)
- `command_type`: a `CliCommandType` object that will be used for all calls to `command` within the group.
- `command_type`：一个 `CliCommandType` 对象，将用于组内对 `command` 的所有调用。
- `kwargs`: any supported kwarg that will be used as the basis for all command calls. Commonly used kwargs include: `custom_command_type` (if custom commands are split amongst many files) and `client_factory` (if custom commands use the `client` argument).
- `kwargs`：任何受支持的 kwarg，将用作所有命令调用的基础。常用的 kwargs 包括：`custom_command_type`（如果自定义命令被分成多个文件）和 `client_factory`（如果自定义命令使用 `client` 参数）。


**(3) Command Registration Helpers**

***command***
```Python
command(self, name, method_name=None, command_type=None, **kwargs)
```

- `name`: The name of the command within the command group
- `name`：命令组内命令的名称
- `method_name`: The name of the SDK or custom method, relative to the path specified in `operations_tmpl`.
- `method_name`：SDK 或自定义方法的名称，相对于 `operations_tmpl` 中指定的路径。
- `command_type`: A `CliCommandType` object to apply to this command (optional).
- `kwargs`: any supported kwarg. Commonly used kwargs include `validator`, `table_transformer ?`, `confirmation 确认`, `supports_no_wait` and  `transform ?`.

Any kwargs that are not specified will be pulled from the `command_type` kwarg, if present.
如果存在，任何未指定的 kwarg 将从 `command_type` kwarg 中提取。

***custom_command***

The signature for `custom_command` is exactly the same as `command`. The only difference is that, whereas `command` uses `command_type` as the fallback for missing kwargs, `custom_command` relies on `custom_command_type`.
`custom_command` 的签名与 `command` 完全相同。唯一的区别是，`command` 使用 `command_type` 作为缺少 kwargs 的后备，而 `custom_command` 依赖于 `custom_command_type`。

***generic_update_command***

See the section on [Generic Update Commands](#generic-update-commands)

***wait_command***

The generic wait command provides a template solution for polling Azure resources until specific conditions are met.
通用等待命令提供了一个模板解决方案，用于在满足特定条件之前轮询 Azure 资源。

```Python
wait_command(self, name, getter_name='get', **kwargs)
```

- `name`: The name of the command within the command group. Commonly called 'wait'.
- `getter_name`: The name of the method for the object getter, relative to the path specified in `operations_tmpl`.
- `getter_name`：对象 getter 的方法名称，相对于 `operations_tmpl` 中指定的路径。
- `kwargs`: any supported kwarg.

Since most wait commands rely on a simple GET call from the SDK, most of these entries simply look like:
```Python
   g.wait_command('wait')
```

***custom_wait_command***

Similar to `custom_command` and `command`, the signature for `custom_wait_command` is exactly the same as `wait_command` but uses `custom_command_type` as the fallback for missing kwargs.

***show_command***

The generic show command ensures a consistent behavior when encountering a missing Azure resource. 
With little exception, all `show` commands should be registered using this method or `custom_show_command` to ensure consistency.
通用 show 命令可确保在遇到丢失的 Azure 资源时行为一致。几乎没有例外，所有 `show` 命令都应该使用此方法或 `custom_show_command` 注册以确保一致性。

```Python
show_command(self, name, getter_name='get', **kwargs)
```

- `name`: The name of the command within the command group. Commonly called 'show'.
- `getter_name`: The name of the method for the object getter, relative to the path specified in `operations_tmpl`.
- `kwargs`: any supported kwarg.

***custom_show_command***

Similar to `custom_command` and `command`, the signature for `custom_show_command` is exactly the same as `show_command` but uses `custom_command_type` as the fallback for missing kwargs.

**(4) Supporting --no-wait**

When registering a command, the boolean `supports_no_wait` property can be used to specify that the command supports `--no-wait`.

Here are examples:

***command()***

```Python
with self.command_group('mymod', mymod_sdk) as g:
    g.command('command1', 'do_something_1', supports_no_wait=True)
```

***custom_command()***

```Python
# inside load_command_table(...)
with self.command_group('mymod', mymod_sdk) as g:
    g.custom_command('command2', 'do_something_2', supports_no_wait=True)

# inside custom.py
from azure.cli.core.util import sdk_no_wait
def do_something_2(cmd, arg1, arg2, no_wait=False):
    return sdk_no_wait(no_wait, client.create_or_update, arg1, arg2)
```

The signature of `azure.cli.core.util.sdk_no_wait` is:

```Python
sdk_no_wait(no_wait, func, *args, **kwargs)
```


- `no_wait` - The boolean for no wait. `True` if `--no-wait` specified. `False` otherwise.
- `func` - The callable to use.
- `args` - The positional arguments that should be passed to the callable.
- `kwargs` - The keyword arguments that should be passed to the callable.

***generic_update_command()***

```Python
with self.command_group('mymod', mymod_sdk) as g:
    g.generic_update_command('update', supports_no_wait=True)
```

**(5) Supporting --defer**

When registering a command, the boolean `supports_local_cache` property can be used to specify that the command supports `--defer`. This will allow traditional GET and PUT requests to interact with the CLI's local object cache instead of making
calls on the wire either for performance reasons (to avoid network latency) or because the service will only accept a payload constructed from many calls.
注册命令时，布尔值 `supports_local_cache` 属性可用于指定命令支持 `--defer推迟`。这将允许传统的 GET 和 PUT 请求与 CLI 的本地对象缓存交互，而不是出于性能原因（以避免网络延迟）或因为服务将仅接受由许多调用构建的有效负载而在线上进行调用。

See [Commands With Complex Types](https://github.com/Azure/azure-cli/blob/dev/doc/command_guidelines.md#commands-with-complex-types)

Here are examples:

***custom_command()***

```Python
# inside load_command_table(...)
with self.command_group('mymod', mymod_sdk) as g:
    g.custom_command('command2', 'do_something_2', supports_local_cache=True)

# inside custom.py
def do_something_2(cmd, client, arg1, arg2, no_wait=False):
    from azure.cli.core.commands import cached_get, cached_put
    item = cached_get(cmd, client.get, arg1, arg2)
    # TODO: perform some mutation of item 执行一些项目的突变
    return cached_put(cmd, client.create_or_update, arg1, arg2, item)
```

Cached objects are deleted upon a successful PUT and can be view and managed using the `az cache` commands.
缓存对象在成功 PUT 后被删除，可以使用 `az cache` 命令查看和管理。

## Write Help Entry

See the following for guidance on writing a help entry: https://github.com/Azure/azure-cli/blob/master/doc/authoring_help.md

## Customize Arguments

While the CLI will attempt to figure out certain key properties of your command and its arguments, it is often necessary to override, add to, or customize this metadata. To modify/enhance your command arguments, create an argument context. For the standard modules, these entries are contained within a file called `_params.py`. Within the `load_arguments` method of your command loader, you will have something like:
虽然 CLI 会尝试找出命令及其参数的某些关键属性，但通常需要覆盖、添加或自定义此元数据。要修改增强命令参数，请创建参数上下文。对于标准模块，这些条目包含在名为“_params.py”的文件中。在你的命令加载器的 `load_arguments` 方法中，你会有类似的东西：

```Python
    # (1) Create an argument context
    with self.argument_context('mymod') as c:
        # (2) Register different kinds of arguments
        c.argument('name', options_list=['--name', '-n'], help='Name of the thing.', completer=get_resource_name_completion_list('Microsoft.Example/mything'))
        c.extra('extra_thing', options_list=['--extra'], help='An extra thing.')
        c.ignore('ignore_this', 'ignore_that')
        c.argument('some_flag', arg_type=get_three_state_flag())
        c.argument('some_enum', arg_type=get_enum_type(MyEnum, default='foo'))
```

For more information:

**(1) Create an argument context**

```Python
argument_context(self, scope, **kwargs):
```

- `scope` - This string is the level at which your customizations are applied. For example, consider the case where you have commands `az mypackage command1` and `az mypackage command2`, which both have a parameter `my_param`.
- `scope` - 此字符串是应用自定义的级别。例如，考虑您有命令 `az mypackage command1` 和 `az mypackage command2` 的情况，它们都有一个参数 `my_param`。

```Python
with self.argument_context('mypackage', ...) as c:  # applies to BOTH command1 and command2
```
But
```Python
with self.argument_context('mypackage command1', ...) as c:  # applies to command1 but not command2
```
Like CSS rules, modifications are applied in order from generic to specific.
与 CSS 规则一样，修改是按从通用到特定的顺序应用的。
应该是指 specific 会覆盖 generic
```Python
with self.argument_context('mypackage', ...) as c:  # applies to both command1 and command2
  c.argument('my_param', ...)
with self.argument_context('mypackage command1', ...) as c:  # applies to command1 but not command2
  c.argument('my_param', ...)
```
- `kwargs` - Any supported kwarg which will be applied to calls within the context block.
- `kwargs` - 任何支持的 kwarg 将应用于上下文块内的调用。

**(2) Register different kinds of arguments**

***argument***
```Python
argument(self, dest, arg_type=None, **kwargs)
```
- `dest` -  The name of the parameter that you are targeting.
- `arg_type` - An instance of the `azure.cli.core.commands.CliArgumentType` class. This essentially serves as a named, reusable packaging of the `kwargs` that modify your command's argument. It is useful when you want to reuse an argument definition, but is generally not required. It is most commonly used for name type parameters, or for enums and flags.
- `arg_type` - `azure.cli.core.commands.CliArgumentType` 类的实例。这本质上用作修改命令参数的`kwargs` 的命名的、可重用的包装。当您想要重用参数定义时它很有用，但通常不是必需的。它最常用于名称类型参数，或用于枚举和标志。
- `kwargs` - Most likely, you will simply specify keyword arguments that will accomplish what you need.  Any `kwargs` specified will override or extended the definition in `arg_type`, if provided.

***ignore***
```Python
ignore(self, *args)
```
- `args` - one or more parameter names (dest values) that should be ignored. Useful to suppress arguments that appear due to reflection on an SDK, but are unwanted in the command signature.
- `args` - 一个或多个应该被忽略的参数名称（目标值）。用于抑制因 SDK 反射而出现但在命令签名中不需要的参数。

***extra***
```Python
extra(self, dest, arg_type=None, **kwargs)
```
Arguments are the same as `argument`, however this will create a new parameter whereas `argument` will not. This is useful when a reflected SDK method is missing a parameter that you need to expose in your command.
参数与 `argument` 相同，但是这会创建一个新参数，而 `argument` 不会。当反射的 SDK 方法缺少您需要在命令中公开的参数时，这很有用。
SDK software development kit 软件开发工具箱

Additional Topics
=============================

## Keyword Argument Reference 关键字参数参考

**Overview of Keyword Arguments in the Azure CLI**

When writing commands for the Azure CLI, it is important to understand how keyword arguments (kwargs) are applied. Refer to the following diagram.

![](/doc/assets/annotated-kwarg-structure.gif)

From the diagram you can see that any kwargs supplied when creating the `AzCommandsLoader` object are passed to and used as the baseline for any command groups or argument contexts that are later created. Any kwargs specified in the `command_group` calls serve as the baseline for any `command` or `custom_command` calls, and any kwargs passed to `argument_context` serve as the baseline for any calls to `argument`.
从图中您可以看到，在创建 `AzCommandsLoader` 对象时提供的任何 kwargs 都被传递给并用作以后创建的任何命令组或参数上下文的基线。在 `command_group` 调用中指定的任何 kwargs 作为任何 `command` 或 `custom_command` 调用的基线，并且任何传递给 `argument_context` 的 kwargs 作为任何对 `argument` 调用的基线。

While kwargs are inherited from higher levels on the diagram, they can be overridden at a lower level. For example, if `custom_command_type=foo` is used as a module-level kwarg in the `AzCommandLoader.__init__` method and `custom_command_type=bar` is passed for a call to `command_group`, then `bar` will be used for all calls to `custom_command` within that command group.

Additionally, you can see that kwargs registered on a command group *do not* carry over to argument contexts, so you must apply the kwargs in both places if necessary.
此外，您可以看到在命令组上注册的 kwargs 不会转移到参数上下文，因此您必须在必要时在两个地方应用 kwargs。

# todo
****Command Group****

_Special Kwargs_

The following special kwargs are supported by command group and its helper methods:
- `table_transformer` - See section on [Custom Table Formats](#custom-table-formats)
- `validator` - See section on [Validators](#validators)
- `confirmation` - During interactive use, will prompt the user to confirm their choice to proceed. Supply a value of True to use the default prompt, or supply a string to use a custom prompt message. If the command is invoked in non-interactive scenarios and the --yes/-y parameter is not supplied, the command will fail.
- `confirmation` - 在交互使用期间，将提示用户确认他们的选择以继续。提供 True 值以使用默认提示，或提供字符串以使用自定义提示消息。如果在非交互式场景中调用该命令并且未提供 --yes-y 参数，则该命令将失败。
- `transform` - Accepts a callable that takes a command result, which can be manipulated as desired. The transformed result is then returned. In general, output formats should closely mirror those returned by the service, and so this should be infrequently used. The modifies the output *regardless of the output format type*.
- `transform` - 接受一个可调用的命令结果，可以根据需要进行操作。然后返回转换后的结果。通常，输出格式应与服务返回的格式密切相关，因此应不经常使用。无论输出格式类型如何，都会修改输出。
- `deprecate_info` - See [Deprecating Commands and Arguments](https://github.com/Azure/azure-cli/blob/dev/doc/authoring_command_modules/authoring_commands.md#deprecating-commands-and-arguments)
- 弃用信息
- `formatter_class` - Advanced. Accepts a custom class that derives from `argparse.HelpFormatter` to modify the help document generation.
- `formatter_class` - 高级。接受从`argparse.HelpFormatter` 派生的自定义类来修改帮助文档生成。
- `argument_loader` - Advanced. Accepts a callable that takes no parameters which will be used in place of the default argument loader.
- `argument_loader` - 高级。接受一个不带参数的可调用对象，这些参数将用于代替默认参数加载器。
- `description_loader` - Advanced. Accepts a callable that takes no parameters which will be used in place of the default description loader.
- `is_preview` - See [Preview Commands and Arguments](https://github.com/Azure/azure-cli/blob/dev/doc/authoring_command_modules/authoring_commands.md#preview-commands-and-arguments)

_General Kwargs_

The following kwargs may be inherited from the command loader:
- `min_api` - Minimum API version for which the command will appear.
- `min_api` - 显示命令的最低 API 版本。
- `max_api` - Maximum API version for which the command will appear.
- `max_api` - 将出现命令的最大 API 版本。
- `resource_type` - An `azure.cli.core.profiles.ResourceType` enum value that is used for multi-API packages.
- `resource_type` - 用于多 API 包的 `azure.cli.core.profiles.ResourceType` 枚举值。
- `operation_group` - Only used by the `azure-cli-vm` module to specify which resource API to target.
- `operation_group` - 仅由 `azure-cli-vm` 模块用于指定要定位的资源 API。
- `command_group` - A `CliCommandType` object that contains a bundle of kwargs that will be used by the `command` method if not otherwise provided.
- `command_group` - 一个 `CliCommandType` 对象，它包含一组 kwargs，如果没有另外提供，`command` 方法将使用这些 kwargs。
- `custom_command_group` - A `CliCommandType` object that contains a bundle of kwargs that will be used by the `custom_command` method if not otherwise provided.
- `custom_command_group` - 一个 `CliCommandType` 对象，它包含一组 kwargs，如果没有另外提供，`custom_command` 方法将使用这些 kwargs。

****Argument Context****

_Special Kwargs_

The follow special kwargs are supported by argument context and its helper methods:
- `options_list` - By default, your argument will be exposed as an option in hyphenated form (ex: `my_param` becomes `--my-param`). If you would like to change the option string without changing the parameter name, and/or add a short option, specify the `options_list` kwarg. This is a list of string values. If there will only be one value, you can just specify the value (Ex: `options_list=['--myparam', '-m']` or `options_list='--myparam'`)
- `options_list` - 默认情况下，您的参数将以带连字符的形式显示为选项（例如：`my_param` 变为 `--my-param`）。如果您想在不更改参数名称的情况下更改选项字符串，或者添加一个短选项，请指定 `options_list` kwarg。这是一个字符串值列表。如果只有一个值，您可以指定该值（例如：`options_list=['--myparam', '-m']` 或 `options_list='--myparam'`）
- `validator` - See section on [Validators](#validators)
- `completer` - See section on [Tab Completion](#tab-completion)
- `id_part` - See section on [Supporting the IDs Parameter](#supporting-the-ids-parameter).
- `arg_group` - Groups arguments within this context under a group name or add an argument to the group. This group name is shown in the help for the command. For example if `arg_group` is "Network", all applicable arguments will be grouped under the heading "Network Arguments" in the help text for the command.
- `arg_group` - 在组名下将此上下文中的参数分组或向组添加参数。该组名显示在命令的帮助中。例如，如果`arg_group` 是“网络”，则所有适用的参数将被分组在命令帮助文本中的“网络参数”标题下。
- `is_preview` - See [Preview Commands and Arguments](https://github.com/Azure/azure-cli/blob/dev/doc/authoring_command_modules/authoring_commands.md#preview-commands-and-arguments)

Additionally, the following `kwargs`, supported by argparse, are supported as well:
此外，argparse支持的这些如下参数，也同样支持：
- `nargs` - See https://docs.python.org/3/library/argparse.html#nargs
- `action` - See https://docs.python.org/3/library/argparse.html#action
- `const` - See https://docs.python.org/3/library/argparse.html#const
- `default` - See https://docs.python.org/3/library/argparse.html#default. Note that the default value is inferred from the parameter's default value in the function signature. If specified, this will override that value.
- 请注意，默认值是从函数签名中参数的默认值推断出来的。如果指定，这将覆盖该值。
- `type` - See https://docs.python.org/3/library/argparse.html#type
- `choices` - See https://docs.python.org/3/library/argparse.html#choices. If specified this will also serve as a value completer for people using tab completion. However, it is not recommended that you use this because the choice lists will be case sensitive. Instead see "Registering Enums".
- 如果指定，这也将作为使用自动补全的值补全。但是，不建议您使用它，因为选择列表将区分大小写。请参阅“注册枚举”。
- `required` - See https://docs.python.org/3/library/argparse.html#required. Note that this value is inferred from the function signature depending on whether or not the parameter has a default value. If specified, this will override that value.
- 请注意，此值是从函数签名中推断出来的，具体取决于参数是否具有默认值。如果指定，这将覆盖该值。
- `help` - See https://docs.python.org/3/library/argparse.html#help. Generally you should avoid adding help text in this way, instead opting to create a help file as described above.
- 通常，您应该避免以这种方式添加帮助文本，而是选择如上所述创建帮助文件。
- `metavar` - See https://docs.python.org/3/library/argparse.html#metavar

_General Kwargs_

The following kwargs may be inherited from the command loader:
- `min_api` - Minimum API version for which the argument will appear. Otherwise the argument will be ignored.
- `max_api` - Maximum API version for which the argument will appear. Otherwise the argument will be ignored.
- `resource_type` - An `azure.cli.core.profiles.ResourceType` enum value that is used for multi-API packages.
- `operation_group` - Only used by the `azure-cli-vm` module to specify which resource API to target.

## Supporting the IDs Parameter

Most ARM resources can be identified by an ID. In many cases, for example `show` and `delete` commands, it may be more useful to copy and paste an ID to identify the target resource instead of having to specify the names of the resource group, the resource, and the parent resource (if any).
大多数 ARM 资源都可以通过 ID 进行标识。在许多情况下，例如 `show` 和 `delete` 命令，复制粘贴 ID 来标识目标资源可能更有用，而不必指定资源组、资源和父资源的名称（如果有的话）。

Azure CLI supports exposing an `--ids` parameter that will parse a resource ID into its constituent named parts so that this parsing need not be done as part of a client script. Additionally `--ids` will accept a _list_ of space-separated IDs, allowing the client to loop the command over each ID.
Azure CLI 支持公开 `--ids` 参数，该参数将资源 ID 解析为其组成的命名部分，因此无需将此解析作为客户端脚本的一部分来完成。此外，`--ids` 将接受空格分隔 ID 的 _list_，允许客户端在每个 ID 上循环命令。

Enabling this functionality only requires the command author specify the appropriate values for `id_part` in their calls to `AzArgumentContext.argument`.
启用此功能只需要命令作者在调用 `AzArgumentContext.argument` 时为 `id_part` 指定适当的值。

Consider the following simplified example for NIC IP config.
考虑以下 NIC IP 配置的简化示例。

```Python
def show_nic_ip_config(resource_group_name, nic_name, ip_config_name):
    # retrieve and return the IP config
    # 获取和返回

# inside load_command_table(...)
with self.command_group('network nic ip-config', network_nic_sdk) as g:
   g.custom_command('show', 'show_nic_ip_config')

# inside load_arguments(...)
with self.argument_context('network nic ip-config') as c:
  c.argument('nic_name', help='The NIC name.')
  c.argument('ip_config_name', options_list=['--name', '-n'], help='The IP config name.')
```
The help output for this command would be:
```
 Arguments
    --name -n          : The IP config name.
    --nic-name         : The NIC name.
    --resource-group -g: Name of resource group.
```

Now let's specify values for the `id_part` kwarg in the calls to `argument`:
现在让我们在对 `argument` 的调用中为 `id_part` kwarg 指定值：
```Python
def show_nic_ip_config(resource_group_name, nic_name, ip_config_name):
    # retrieve and return the IP config

# inside load_command_table(...)
with self.command_group('network nic ip-config', network_nic_sdk) as g:
   g.custom_command('show', 'show_nic_ip_config')

# inside load_arguments(...)
with self.argument_context('network nic ip-config') as c:
  c.argument('nic_name', help='The NIC name.', id_part='name')
  c.argument('ip_config_name', id_part='child_name_1', options_list=['--name', '-n'], help='The IP config name.')
```
The help output becomes:
```
Arguments

Resource Id Arguments
    --ids              : One or more resource IDs. If provided, no other 'Resource Id' arguments
                         should be specified.
                         一个或多个资源 ID。如果提供，则不应指定其他“资源 ID”参数。
    --name -n          : The IP config name.
    --nic-name         : The NIC name.
    --resource-group -g: Name of resource group.
```
Now the user may identify the target IP config by specifying either the resource group, NIC and IP config names or by simply pasting in the ID for the IP config itself.
现在，用户可以通过指定资源组、NIC 和 IP 配置名称或通过简单地粘贴 IP 配置本身的 ID 来识别目标 IP 配置。

This feature is powered by the `parse_resource_id` helper method within the `msrestazure` package, which parses a resource ID into a dictionary. Specifying `id_part` maps the parsed value for a given key in that dictionary into your argument.
此功能由 `msrestazure` 包中的 `parse_resource_id` 辅助方法提供支持，该方法将资源 ID 解析为字典。指定 `id_part` 将该字典中给定键的解析值映射到您的参数中。

For example, consider the following ID of a subnet lock:
```
subscription/0000-0000-0000-0000/resourceGroups/myresourcegroup/Microsoft.Network/virtualNetworks/myvnet/subnets/mysubnet /providers/Microsoft.Authorization/locks/mylock
```

When run through `parse_resource_id`, the following dictionary results:
```Python
{
    "subscription": "0000-0000-0000-0000",
    "resource_group": "myresourcegroup",
    "namespace": "Microsoft.Network",
    "resource_type": "virtualNetworks",
    "name": "myvnet",
    "child_type_1": "subnets",
    "child_name_1": "mysubnet",
    "child_namespace_2": "Microsoft.Authorization",
    "child_type_2": "locks",
    "child_name_2": "mylock"
}
```

Any of these keys could be supplied as a value for `id_part`, thought typically you would only use `name`, `child_name_1`, `child_name_2`, etc.
这些键中的任何一个都可以作为`id_part`的值提供，通常认为你只会使用`name`、`child_name_1`、`child_name_2`等。

A couple things to note:
- Currently, `--ids` is not exposed for any command that is called 'create', even if it is configured properly.
- 目前，即使配置正确，也不会为任何名为“create”的命令公开 `--ids`。
- `--ids` is intended to be the ID of the resource the command group is about. Thus, it needs to be suppressed on `list` commands for child resources. This simplest way to do this:
- `--ids` 旨在作为命令组所涉及的资源的 ID。因此，需要在子资源的 `list` 命令上抑制它。这种最简单的方法来做到这一点：
```Python
with self.argument_context('parent child') as c:
  c.argument('parent_name', id_part=None)  # This should ALWAYS be the id_part that was 'name'.
  c.argument('child_name', ...)
```

## Supporting Name or ID Parameters

Often times, the service needs references to supporting resources like storage accounts, key vault, etc. Typically, services require the ARM ID of these resources. The CLI pattern is to accept the ARM ID for this resource OR the name of the resource, assuming the resource is in the same subscription and resource group as the main resource.
很多时候，服务需要引用支持资源，如存储帐户、密钥保管库等。通常，服务需要这些资源的 ARM ID。 CLI 模式是接受此资源的 ARM ID 或资源名称，假设资源与主资源在同一订阅和资源组中。

DO NOT:
- Expose an ID parameter like `--storage-account-id`.
- Add parameters like `--storage-account-resource-group` to indicate the resource group for the secondary resource. The user should supply the ARM ID in this instance.
- 添加`--storage-account-resource-group`等参数以指示辅助资源的资源组。在这种情况下，用户应提供 ARM ID。
- # todo 什么是ARM

DO:
- Call the parameter `--storage-account` and indicate in the help text that it accepts the "Name or ID of the storage account."
- 调用参数 `--storage-account` 并在帮助文本中指明它接受“存储帐户的名称或 ID”。
- Add logic similar to the following to a validator or custom command to process the name or ID logic:
- 将类似于以下的逻辑添加到验证器或自定义命令以处理名称或 ID 逻辑：

**Custom Command**
```Python
def my_command(cmd, resource_group_name, foo_name, storage_account):
    from azure.cli.core.commands.client_factory import get_subscription_id
    from msrestazure.tools import is_valid_resource_id, resource_id
    if not is_valid_resource_id(storage_account):
        storage_account = resource_id(
            subscription=get_subscription_id(cmd.cli_ctx),
            resource_group=resource_group_name,
            namespace='Microsoft.Storage', type='storageAccounts',
            name=storage_account
        )
```

**Validator**
```Python
def validate_storage_name_or_id(cmd, namespace):
    from azure.cli.core.commands.client_factory import get_subscription_id
    from msrestazure.tools import is_valid_resource_id, resource_id
    if namespace.storage_account:
        if not is_valid_resource_id(namespace.storage_account):
            namespace.storage_account = resource_id(
                subscription=get_subscription_id(cmd.cli_ctx),
                resource_group=namespace.resource_group_name,
                namespace='Microsoft.Storage', type='storageAccounts',
                name=namespace.storage_account
            )
```


## Generic Update Commands

The update commands within the CLI expose a set of generic update arguments: `--add`, `--remove` and `--set`. This allows the user to manipulate objects in a consistent way that may not have long option flags supported by the command. The method which exposes these arguments is `AzCommandGroup.generic_update_command` in the `azure.cli.core.commands` package. The signature of this method is:
CLI 中的更新命令公开了一组通用更新参数：`--add`、`--remove` 和 `--set`。这允许用户以一致的方式操作对象，这些对象可能没有命令支持的长选项标志。公开这些参数的方法是 `azure.cli.core.commands` 包中的 `AzCommandGroup.generic_update_command`。这个方法的签名是：
# todo

```Python
generic_update_command(self, name,
                       getter_name='get', getter_type=None,
                       setter_name='create_or_update', setter_type=None, setter_arg_name='parameters',
                       child_collection_prop_name=None, child_collection_key='name', child_arg_name='item_name',
                       custom_func_name=None, custom_func_type=None, **kwargs)
```

Since most generic update commands can be reflected from the SDK, the simplest form this command can take is:
由于大多数通用更新命令都可以从 SDK 中反映出来，因此该命令可以采用的最简单形式是：
```Python
with self.command_group('test', test_sdk) as g:
  g.generic_update_command('update')
```

However, most commonly, the `custom_func_name` and `custom_func_type` kwargs will be used to expose convenience arguments in addition to the generic arguments.
然而，最常见的是，除了通用参数之外，`custom_func_name` 和 `custom_func_type` kwargs 将用于公开便利参数。

- `name` - The name of the command. Most commonly 'update'.
- `getter_name` - The name of the method which will be used to retrieve the object instance. If the method is named `get` (which is the case for most SDKs), this can be omitted.
- `getter_name` - 将用于检索对象实例的方法的名称。如果该方法名为`get`（大多数SDK 都是这种情况），则可以省略。
- `getter_type` - A `CliCommandType` object which will be used to locate the getter. Only needed if the getter is a custom command (uncommon).
- `getter_type` - 一个 `CliCommandType` 对象，用于定位 getter。仅当 getter 是自定义命令时才需要（不常见）。
- `setter_name` - The name of the method which will be used to update the object instance using a PUT method. If the method is named `create_or_update` (which is the case for most SDKs), this can be omitted.
- `setter_name` - 将用于使用 PUT 方法更新对象实例的方法的名称。如果该方法名为“create_or_update”（大多数 SDK 都是这种情况），则可以省略。
- `setter_type` - A `CliCommandType` object which will be used to locate the setter. Only needed if the setter is a custom command (uncommon).
- `setter_type` - 用于定位 setter 的 `CliCommandType` 对象。仅当 setter 是自定义命令时才需要（不常见）。
- `setter_arg_name` - The name of the argument in the setter which corresponds to the object being updated. If the name is `parameters` (which is the case for most SDKs), this can be omitted.
- `setter_arg_name` - 对应于正在更新的对象的 setter 中的参数名称。如果名称是 `parameters`（大多数 SDK 都是这种情况），则可以省略此项。
- `custom_func_name` (optional) - The name of a method which accepts the object being updated (must be named `instance`), mutates, and returns that object. This is commonly used to add convenience options to the command by listing them in the method signature, similar to a purely custom method. The difference is that a custom command function returns the command result while a generic update custom function returns only the object being updated. A simple custom function might look like:
- `custom_func_name`（可选） - 接受正在更新的对象（必须命名为 `instance`）、变异并返回该对象的方法的名称。这通常用于通过在方法签名中列出它们来向命令添加便利选项，类似于纯自定义方法。区别在于自定义命令函数返回命令结果，而通用更新自定义函数仅返回正在更新的对象。一个简单的自定义函数可能如下所示：

  ```Python
  def my_custom_function(instance, item_name, custom_arg=None):
    if custom_arg:
        instance.property = custom_arg
    return instance
  ```
  In this case the `custom_func_name` would be `my_custom_function`.
- `custom_func_type` - A `CliCommandType` object which will be used to locate the custom function. If omitted, the CLI will look for and attempt to use the `custom_command_type` kwarg.
- `custom_func_type` - 一个 `CliCommandType` 对象，用于定位自定义函数。如果省略，CLI 将查找并尝试使用 `custom_command_type` kwarg。
- `kwargs` - Any valid command kwarg.

**Working With Child Collections and Properties (Advanced)**
# 使用子集合和属性（高级）

Sometimes you will want to write commands that operate on child resources and it may be that these child resources don't have dedicated getters and setters. In these cases, you must rely on the getter and setter of the parent resource. For example, consider an object `my_parent` which has a child collection `my_child` which in turn has its own child collection `my_grandchild`. The key property for all of these objects is simply `name`. For these cases, `generic_update_command` has three additional parameters:
有时您会想要编写对子资源进行操作的命令，而这些子资源可能没有专用的 getter 和 setter。在这些情况下，您必须依赖父资源的 getter 和 setter。例如，考虑一个对象“my_parent”，它有一个子集合“my_child”，而它又拥有自己的子集合“my_grandchild”。所有这些对象的关键属性只是“名称”。对于这些情况，`generic_update_command` 有三个附加参数：
  - `child_collection_prop_name` - the name path to the child collection property, using dot syntax. To access `my_child`, the value would be `my_child`. To access `my_grandchild`, the value would be `my_child.my_grandchild`.
  - `child_collection_prop_name` - 子集合属性的名称路径，使用点语法。要访问“my_child”，该值将是“my_child”。要访问“my_grandchild”，该值将是“my_child.my_grandchild”。
  - `child_collection_key` - Most child collections in Azure are lists of objects (as opposed to dictionaries) which will have a property in them that serves as the key. This is the name of that key property. By default it is `name`. To refer to `my_child`, the value would be `name`. To refer to `my_grandchild` the value would be `name.name`.
  - `child_collection_key` - Azure 中的大多数子集合是对象列表（与字典相反），其中将有一个用作键的属性。这是该键属性的名称。默认情况下它是`name`。要引用`my_child`，值应该是`name`。要引用`my_grandchild`，值应该是`name.name`。
  - `child_arg_name` - If you want to refer the child object key (the property identified by `child_collection_key`) inside a custom function, you should specify the argument name you use in your custom function. By default, this is called `item_name`. In the above example, where our child object had a key called `name`, you could refer to this property within your custom function through the `item_name` property, or specify something different. For grandchild collections, use dot syntax (i.e.: `child_name.grandchild_name`).
  - `child_arg_name` - 如果要在自定义函数中引用子对象键（由 `child_collection_key` 标识的属性），则应指定在自定义函数中使用的参数名称。默认情况下，这称为“item_name”。在上面的例子中，我们的子对象有一个名为 `name` 的键，你可以通过 `item_name` 属性在你的自定义函数中引用这个属性，或者指定一些不同的东西。对于孙子集合，请使用点语法（即：`child_name.grandchild_name`）。

**Logic Flow**
# 逻辑流程

A simplified understanding of the flow of the generic update is as follows:
通用更新流程的简单理解如下：

```Python
instance = getter(...)  # retrieve the object
if custom_function:
    instance = custom_function(...) # apply custom logic
instance = _process_generic_updates(...) # apply generic updates, which will overwrite custom logic in the event of a conflict
return setter(instance)  # update the instance and return the result
```

**Generic Update for PATCH-based Services**
基于 PATCH 的服务的通用更新

`generic_update_command` was designed to simulate PATCH-like behavior for services that are backed only by a PUT API endpoint. For services that have actual PATCH-based update endpoints, the CLI's `update` command should still leverage `generic_update_command` in order to provide consistency among commands. The following guidelines should be helpful:
`generic_update_command` 旨在为仅由 PUT API 端点支持的服务模拟类似 PATCH 的行为。对于具有实际基于 PATCH 的更新端点的服务，CLI 的 `update` 命令仍应利用 `generic_update_command` 以提供命令之间的一致性。以下指南应该会有所帮助：

- You'll probably need to specify the `setter_name` since it will likely be `update` instead of `create_or_update` (the default).
- 您可能需要指定 `setter_name`，因为它可能是 `update` 而不是 `create_or_update`（默认值）。
- You will HAVE TO supply `custom_func_name` and `custom_func_type`. Consider the following example:
- 您必须提供 `custom_func_name` 和 `custom_func_type`。考虑以下示例：
```Python
def my_custom_foo_update(instance, prop1=None, prop2=None, complex_prop1=None, complex_prop2=None):
   from my_foo_sdk import FooUpdateParameters, ComplexProperty

   # (1) instantiate the update parameters object. Generally, you can pass simple parameters
   # 实例化更新参数对象。一般可以传递简单的参数
   # as-is and the service will correctly interpret this.
   # 按原样，服务将正确解释这一点。
   parameters = FooUpdateParameters(
     prop1=prop1,
     prop2=prop2)

   # (2) complex objects must also have PATCH-like behavior, and often services do not
   # correctly support this. You may need to fill these objects with the existing
   # values if they are not being updated
   # (2) 复杂的对象也必须有类似 PATCH 的行为，而服务往往不能正确支持这一点。如果它们没有被更新，您可能需要用现有值填充这些对象
   parameters.complex_prop = ComplexProperty(
     complex_prop1=complex_prop1 or instance.complex_prop.complex_prop1,
     complex_prop2=complex_prop2 or instance.complex_prop.complex_prop2
   )
   # (3) instead of returning the instance object as you do with a PUT-based generic update,
   # return the update parameters object.
   # (3) 不是像使用基于 PUT 的通用更新那样返回实例对象，而是返回更新参数对象。
   return parameters
```

## Custom Table Formats
自定义表格格式

By default, when the `-o/--output table` option is supplied, the CLI will display the top level fields of the object structure as the columns of the table. The user can always specify a `--query` to control table and TSV formats, but the CLI also allows the command author to specify a different default table format. Two options exist:
默认情况下，当提供`-o--output table` 选项时，CLI 将对象结构的顶级字段显示为表的列。用户始终可以指定 `--query` 来控制表和 TSV 格式，但 CLI 还允许命令作者指定不同的默认表格式。存在两种选择：

**Supply a Callable**

Supply a callable that accepts the result as input and returns a list of OrderedDicts:
提供一个接受结果作为输入并返回 OrderedDicts 列表的可调用对象：

```Python
def transform_foo(result):
    result = OrderedDict([('name', result['name']),
                          ('resourceGroup', result['resourceGroup']),
                          ('location', result['location'])])
    return result
```

**Supply a JMESPath String**

A string containing Python dictionary-syntax '{Key:JMESPath path to property, ...}'
包含 Python 字典语法 '{Key:JMESPath path to property, ...}' 的字符串

Example:
```Python
table_transformer='{Name:name, ResourceGroup:resourceGroup, Location:location, ProvisioningState:provisioningState, PowerState:instanceView.statuses[1].displayStatus}'
```

## Tab Completion

Tab completion is enabled by default (in bash or `az interactive`) for command names, argument names and argument choice lists. To enable tab completion for dynamic properties (for example, resource names) you can supply a callable which returns a list of options:
默认情况下（在 bash 或 `az interactive` 中）为命令名称、参数名称和参数选择列表启用自动补全。要为动态属性（例如，资源名称）启用自动补全，您可以提供一个可调用的返回选项列表的可调用对象：

**get_resource_name_completion_list(resource_type)**

Since many completers simply return a list of resource names, you can use the `get_resource_name_completion_list` method from `azure.cli.core.commands.parameters` which accepts the type of resource you wish to get completions for.
由于许多补全只返回一个资源名称列表，您可以使用 `azure.cli.core.commands.parameters` 中的 `get_resource_name_completion_list` 方法，该方法接受您希望获得补全的资源类型。

Example:
```Python
completer=get_resource_name_completion_list('Microsoft.Compute/virtualMachines')
```

The behavior of the completer will depend on what the user has entered prior to hitting [TAB][TAB].  For example:
补全的行为将取决于用户在点击 [TAB][TAB] 之前输入的内容。例如：
`az vm show -n [TAB][TAB]`
This will show VM names within the entire subscription.
这将显示整个订阅中的 VM 名称。
`az vm show -g myrg -n [TAB][TAB]`
This will show VM names only within the provided resource group.
这将仅在提供的资源组中显示 VM 名称。

**Custom Completer**

```Python
from azure.cli.core.decorators import Completer

@Completer
def get_foo_completion_list(cmd, prefix, namespace, **kwargs):  # pylint: disable=unused-argument
    # TODO: Your custom logic here
    result = ...
    return [r.name for r in result]
```

The method signature must be as shown and it must return a list of names. You also must use the `@Completer` decorator. You can make additional REST calls within the completer and may examine the partially processed namespace via `namespace` to filter the list based on already supplied args (as in the above case with VM).
方法签名必须如图所示，并且必须返回名称列表。您还必须使用 `@Completer` 装饰器。您可以在补全程序中进行额外的 REST 调用，并且可以通过“namespace”检查部分?处理?的命名空间，以根据已提供的参数来过滤列表（如上述 VM 的情况）。

## Validators

Validators are custom pieces of code that allow you to perform any custom logic or validation on the entire namespace prior to command execution. Their structure is as follows:
验证器是自定义代码段，允许您在命令执行之前对整个命名空间执行任何自定义逻辑或验证。它们的结构如下：

```Python
def validate_my_arg(namespace):
   if namespace.foo:
      # TODO: Your custom logic here
      ...
```

If you need access to the `cli_ctx` within your validator (for instance, to make additional REST calls) the following signature can be used:

```Python
def validate_my_arg(cmd, namespace):
   if namespace.foo:
      # TODO: Your custom logic here
      client=my_client_class(cmd.cli_ctx)
      ...
```

Validators are executed after argument parsing, and thus after the native argparse-supported `type` and `action` have been applied. A CLIError raised during a validator execution will be treated as a validation error, which will result in the display of the command usage string, as opposed to the same error raised within a custom command, which will just print the error and no validation string.
验证器在参数解析后执行，因此在应用了原生 argparse 支持的 `type` 和 `action` 之后。在验证程序执行期间引发的 CLIError 将被视为验证错误，这将导致显示命令使用字符串，而不是在自定义命令中抛出相同的错误，后者只会打印错误而没有验证字符串。

***Command Validators***
The `validator` keyword applies to commands and arguments. A command can have, at most, one validator. If supplied, then *only* this validator will be executed. Any argument-level validators will be ignored. The reason to use a command validator is if the validation sequence is important.  However, the command validator can and very often is composed to individual argument level validators. You simply define the sequence in which they execute.
`validator` 关键字适用于命令和参数。一个命令最多可以有一个验证器。如果提供，则仅执行此验证器。任何参数级验证器都将被忽略。使用命令验证器的原因是：验证序列是否重要。但是，命令验证器可以并且经常由单独的参数级别验证器组成。您只需定义它们执行的顺序。

***Argument Validators***
An argument can be assigned, at most, one validator. However, since a command can have many arguments, this means that a command can have many argument validators. Furthermore, since an argument context may apply to many commands, this means that this argument validator can be reused across many commands. At execution time, argument validators are executed *in random order*, so you should ensure you do not have dependencies between validators. If you do, the a command validator is the appropriate route to take. It is fine to have an argument validator involve several parameters as long as they are interdependent (for example, a validator involving a vnet name and subnet name).
一个参数最多可以分配一个验证器。然而，由于一个命令可以有很多参数，这意味着一个命令可以有很多参数验证器。此外，由于参数上下文可能适用于许多命令，这意味着该参数验证器可以在许多命令中重复使用。在执行时，参数验证器以随机顺序执行，因此您应该确保验证器之间没有依赖关系。如果这样做，则命令验证器是合适的选择。一个参数验证器可以包含多个参数，只要它们是相互依赖的（例如，一个包含 vnet 名称和子网名称的验证器）。

## Registering Flags

The recommended way to register boolean properties in the CLI is using the `get_three_state_flag` arg_type.
在 CLI 中注册布尔属性的推荐方法是使用 `get_three_state_flag` arg_type。

```Python
with self.argument_context('mymod') as c:
  c.argument('bool_prop_enabled', arg_type=get_three_state_flag())
```

This will allow the user to specify the option as a flag or as a true/false parameter and allows for maximum convenience and consistency between create and update commands.  With the above registration, the following inputs would be accepted:
这将允许用户将选项指定为标志或 true/false 参数，并允许创建和更新命令之间的最大便利性和一致性。通过上述注册，将接受以下输入：

```
az mymod --bool-prop-enabled       # bool_prop_enabled = TRUE
az mymod --bool-prop-enabled true  # bool_prop_enabled = TRUE
az mymod --bool-prop-enabled false # bool_prop_enabled = FALSE

```

For flags that are switches on the command itself and not persisted as properties of a resource, the flag should be registered as follows:
对于作为命令本身的开关且不作为资源属性持久化的标志，应按如下方式注册该标志：

```Python
with self.argument_context('mymod') as c:
  c.argument('command_switch', action='store_true')
```

In this case, it will only accept the flag form. Do not use this for boolean properties.
在这种情况下，它将只接受标志形式。不要将此用于布尔属性。

## Registering Enums

The recommended way to register enums (either reflected from an SDK or custom choice lists) is to use the `get_enum_type` arg_type.
注册枚举的推荐方法（从 SDK 或自定义选择列表反映）是使用 `get_enum_type` arg_type。

```Python
from azure.mgmt.mymod.models import MyModelEnum

with self.argument_context('mymod') as c:
  c.argument('my_enum', arg_type=get_enum_type(MyModelEnum))
  c.argument('my_enum2', arg_type=get_enum_type(['choice1', 'choice2']))
```

Above are two examples of how this can be used. In the first instance, an Enum model is reflected from the SDK. In the second instance, a custom choice list is provided. This is preferable to using the native `argparse.choices` kwarg because the choice lists generated by `get_enum_type` will be case insensitive.
以上是如何使用它的两个示例。在第一个实例中，一个 Enum 模型从 SDK 中反映出来。在第二种情况下，提供自定义选择列表。这比使用原生 `argparse.choices` kwarg 更可取，因为 `get_enum_type` 生成的选择列表将不区分大小写。

## Extension Suppression
扩展抑制

It is possible for a command module to suppress specific extensions from being loaded.
命令模块可以禁止加载特定的扩展。
This is useful for commands that were once extensions that have now moved inside a command module.
这对于曾经是扩展现在移动到命令模块中的命令很有用。
Here, we suppress an extension by name and also by version.
在这里，我们按名称和版本抑制扩展。
This will allow the extension to be published in the future with the same name and a newer version that will not be suppressed.
这将允许使用相同的名称和更新版本扩展得已发布，而不会被抑制。
This is great for experimental extensions that periodically get incorporated into the product.
这对于定期合并到产品中的实验性扩展非常有用。

```Python
class MyCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core import ModExtensionSuppress
        # Suppress myextension up to and including version 0.2.0
        super(MyCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                               suppress_extension=ModExtensionSuppress(__name__, 'myextension', '0.2.0',
                                                                                       reason='These commands are now in the CLI.',
                                                                                       recommend_remove=True))
```

## Deprecating Commands and Arguments
弃用命令和参数

The CLI has built-in support for deprecating the following: commands, command groups, arguments, option values. Deprecated items will appear with a warning in the help system or when invoked. The following keyword arguments are supported when deprecating an item:
CLI 内置支持弃用以下内容：命令、命令组、参数、选项值。不推荐使用的项目将在帮助系统中或在调用时显示警告。弃用项目时支持以下关键字参数：

- `target`: The thing being deprecated. This is often not needed as in most cases the CLI can figure out what is being deprecated.
- `redirect`: This is the alternative that should be used in lieu of the deprecated thing. If not provided, the item is expected to be removed in the future with no replacement.
- `redirect`：这是应该用来代替不推荐使用的东西的替代方法。如果未提供，则预计该项目将来会被移除而无需更换。
- `hide`: Hide the deprecated item from the help system, reducing discoverability, but still allow it to be used. Accepts either the boolean `True` to immediately hide the item or a core CLI version. If a version is supplied, the item will appear until the core CLI rolls to the specified value, after which it will be hidden.
- `hide`：从帮助系统中隐藏已弃用的项目，降低可发现性，但仍允许使用它。接受布尔值“True”以立即隐藏项目或核心 CLI 版本。如果提供了一个版本，该项目将一直显示，直到核心 CLI 滚动到指定的值，之后它将被隐藏。
- `expiration`: Accepts a core CLI version at which the deprecated item will no longer function. This version will be communicated in all warning messages. 
- `expiration`：接受一个核心 CLI 版本，在该版本中已弃用的项目将不再起作用。此版本将在所有警告消息中传达。

Deprecation of different command elements are usually accomplished using the `deprecate_info` kwarg in conjunction with a `deprecate` helper method.
不同命令元素的弃用通常是使用 `deprecate_info` kwarg 和 `deprecate` 辅助方法来完成的。

***Deprecate Command Group***
```Python
with self.command_group('test', test_sdk, deprecate_info=self.deprecate(redirect='new-test', hide=True)) as g:
  g.show_command('show', 'get')
  g.command('list', 'list')
```

This will deprecate the entire command group `test`. Note that call to `self.deprecate`, calling the deprecate helper method off of the command loader. The warning message for this would read: ```This command group has been deprecated and will be removed in a future release. Use `new-test` instead.```
这将弃用整个命令组“test”。请注意调用`self.deprecate`，从命令加载器中调用deprecate helper 方法。此警告消息将显示为：```此命令组已被弃用，并将在未来版本中删除。改用`new-test`。```

Additionally, since the command group is deprecated then, by extension, all of the commands within it are deprecated as well. They will not be marked as such, but will display a warning:
此外，由于命令组已被弃用，因此通过扩展，其中的所有命令也将被弃用。它们不会被标记为这样，但会显示警告：

```This command has been implicitly deprecated because command group `test` is deprecated and will be removed in a future release. Use `new-test` instead.```
```此命令已被隐式弃用，因为命令组 `test` 已弃用，并将在未来版本中删除。改用`new-test`。```

***Deprecate Command***
```Python
with self.command_group('test', test_sdk) as g:
  g.command('show-parameters', 'get_params', deprecate_info=g.deprecate(redirect='test show', expiration='2.1.0'))
```

This will deprecate the command `test show-parameters`. Note that call to `g.deprecate`, calling the deprecate helper method off of the command group. The warning message for this would read: ```This command has been deprecated and will be removed in version 2.1.0. Use `test show` instead.```
这将弃用命令`test show-parameters`。请注意调用`g.deprecate`，从命令组中调用deprecate helper 方法。警告消息将显示为：```此命令已被弃用，并将在 2.1.0 版中删除。改用`test show`。```

***Deprecate Argument***
```Python
with self.argument_context('test show-parameters') as c:
  c.argument('junk_flag', help='Something we no longer want to support.' deprecate_info=c.deprecate(expiration='2.1.0'))
```

This will deprecate the argument `--junk-flag` on `test show-parameters`. Note that call to `c.deprecate`, calling the deprecate helper method off of the argument context. The warning message for this would read: ```Argument `--junk-flag` has been deprecated and will be removed in version 2.1.0.```
这将弃用 `test show-parameters` 上的参数 `--junk-flag`。请注意，调用 `c.deprecate`，从参数上下文中调用 deprecate 辅助方法。警告消息将显示为：```Argument `--junk-flag` 已被弃用，将在 2.1.0 版中删除。```

***Deprecate Argument Option***
```Python
with self.argument_context('test show-parameters') as c:
  c.argument('resource', options_list=['--resource', c.deprecate(target='--resource-id', redirect='--target')])
```

This will deprecate the argument `--resource-id` option on `test show-parameters` in favor of `--resource`. Note that call to `c.deprecate`, calling the deprecate helper method off of the argument context. The warning message for this would read: ```Option `--resource-id` has been deprecated and will be removed in a future release. Use `--resource` instead.``` Here you must specify `target` in order to identify the deprecated option. When an option value is deprecated, it appears in help as two separate arguments, with the deprecation warning on the deprecated option. 
这将弃用 `test show-parameters` 上的参数 `--resource-id` 选项，转而使用 `--resource`。请注意，调用 `c.deprecate`，从参数上下文中调用 deprecate 辅助方法。此警告消息将显示为：```Option `--resource-id` 已被弃用，并将在未来版本中删除。使用 `--resource` 代替。``` 这里你必须指定 `target` 以识别不推荐使用的选项。当一个选项值被弃用时，它作为两个单独的参数出现在帮助中，弃用的选项上带有弃用警告。

## Multi-API Aware Modules
多 API 感知模块
To convert a module that used a mono-versioned SDK to one that works with multiple API versions:
要将使用单版本 SDK 的模块转换为适用于多个 API 版本的模块：

1. In `azure.cli.core.profiles._shared.py` register your SDK and client in the `ResourceType` enum:

```Python
class ResourceType(Enum):

  MGMT_MYSERVICE = ('azure.mgmt.myservice, MyServiceManagementClient')  # REGISTER YOUR SDK
  ...
```


2. In the `AZURE_API_PROFILES` dictionary in that same file, for each profile your service applies to, add an entry for it like this:
对于您的服务适用的每个配置文件，为它添加一个条目，如下所示
```Python
AZURE_API_PROFILES = {
  'latest': {
    ResourceType.MGMT_MYSERVICE: '2019-03-01' # the supported API version on that profile
    ...
  },
  '2020-09-01-hybrid': {
    ResourceType.MGMT_MYSERVICE: '2018-08-01' # different API version for this profile
    ...
  },
  ...
}
```

3. Update imports in your files. They must use the API profile-aware "get_models" method and have access to a command or CLI object.
更新文件中的导入。他们必须使用 API 配置文件感知“get_models”方法并有权访问命令或 CLI 对象。

Example:
```Python
from azure.mgmt.myservice import Foo, Boo

def my_command(...):
   # do stuff
```

Converted:
```Python
def my_command(cmd, ...):
  Foo, Boo = cmd.get_models('Foo', 'Boo')
  # do stuff
```

4. Use appropriate conditionals to ensure your command can run on all supported profiles:
使用适当的条件来确保您的命令可以在所有支持的配置文件上运行：

***commands.py***

```Python
with self.command_group('test') as g:
  g.command('use-new-feature', 'use_new_feature', min_api='2018-03-01')  # won't be available unless min API is met
```

***params.py***

```Python
with self.argument_context('test create') as c:
  c.argument('enable_new_feature', min_api='2018-03-01', arg_type=get_three_state_flag())  # expose argument only when min API is satisfied
```

***custom.py***

```Python
def my_test_command(cmd, ...):
  Foo = cmd.get_models('Foo')
  my_foo = Foo(...)
  
  # will still work with older API versions because this branch will be skipped
  if cmd.supported_api_version(min_api='2018-03-01'):
    my_foo.enable_new_feature = enable_new_feature

  return client.create_or_update(..., my_foo)
```

See earlier topics for other kwargs that can be used with multi-API idioms.
有关可与多 API 习语一起使用的其他 kwarg，请参阅之前的主题。

## Preview Commands and Arguments
预览命令和参数

The CLI has built-in support for marking commands, command groups and arguments as being in "preview" status. Preview items will appear with a warning in the help system or when invoked. Items marked preview can be changed, broken or removed at any time without following the deprecation process. 
CLI 内置支持将命令、命令组和参数标记为处于“预览”状态。预览项目将在帮助系统中或在调用时显示警告。可以随时更改、破坏或删除标记为预览的项目，而无需遵循弃用流程。

**Note that ANYTHING not marked "preview" is considered GA and thus a breaking change can only be enacted by following the deprecation mechanism (see earlier topic).**
请注意，任何未标记为“预览”的内容都被视为 GA，因此只能通过遵循弃用机制（请参阅前面的主题）来制定重大更改。
GA General Availability，代表官方开始推荐广泛使用。

Items are marked Preview using the `is_preview=True` kwarg. See the following for examples:
项目使用 `is_preview=True` kwarg 标记为预览。请参阅以下示例：

***Preview Command Group***
```Python
with self.command_group('test', test_sdk, is_preview=True) as g:
  g.show_command('show', 'get')
  ...
```

Additionally, since the command group is in preview then, by extension, all of the commands and arguments within it are in preview as well. No message will be displayed for implicitly in-preview arguments, but a warning will be displayed for implicitly in-preview commands.
此外，由于命令组处于预览状态，因此通过扩展，其中的所有命令和参数也处于预览状态。不会为隐式预览参数显示任何消息，但会为隐式预览命令显示警告。

***Preview Command***
```Python
with self.command_group('test', test_sdk) as g:
  g.command('show-parameters', 'get_params', is_preview=True)
```

This will declare just the command `test show-parameters` as being in preview. This command will appear with the `[Preview]` status tag when viewed in group help whereas other commands in the `test` group will not, indicating that only this command (and, by implication, its arguments) are in preview status.
这将仅将命令 `test show-parameters` 声明为处于预览状态。在组帮助中查看时，此命令将显示为带有“[Preview]”状态标签，而“test”组中的其他命令则不会，这表明只有此命令（以及其参数）处于预览状态。

***Preview Argument***
```Python
with self.argument_context('test show-parameters') as c:
  c.argument('cool_flag', help='Something cool new flag.', is_preview=True)
```

This will mark the argument `--cool-flag` on `test show-parameters` as being in preview, appearing with the `[Preview]` tag.
这会将 `test show-parameters` 上的参数 `--cool-flag` 标记为处于预览状态，并带有 `[Preview]` 标签。

***Preview Extensions***

Extensions are marked as being in preview using an older mechanism in the `azext_metadata.json` file.
使用 `azext_metadata.json` 文件中的旧机制将扩展标记为处于预览状态。

```
{
    "azext.isPreview": true,
}
```

It is recommended that, if an extension is in preview, that it also uses the above mechanisms to give the same level of visibility to in preview items.
如果扩展处于预览状态，建议它也使用上述机制为预览项目提供相同级别的可见性。
