Authoring Command Modules  
创作命令模块  
=========================  
The document provides instructions and guidelines on how to author command modules. For other help, please see the following:
该文档提供了有关如何编写命令模块的说明和指南。如需其他帮助，请参阅以下内容：
**On-boarding Guide**:<br>https://github.com/Azure/azure-cli/blob/dev/doc/onboarding_guide.md

**Module Authoring**:<br>You are here!

**Command Authoring**:<br>https://github.com/Azure/azure-cli/blob/dev/doc/authoring_command_modules/authoring_commands.md

**Command Guidelines**:<br>https://github.com/Azure/azure-cli/blob/dev/doc/command_guidelines.md

**Help Authoring**:<br>https://github.com/Azure/azure-cli/blob/dev/doc/authoring_help.md

**Test Authoring**:<br>https://github.com/Azure/azure-cli/blob/dev/doc/authoring_tests.md

**Generating Documentation**:<br>https://review.docs.microsoft.com/help/onboard/admin/reference/cli/azure-cli-ci?branch=master#documenting-a-new-azure-cli-module

<a name="heading_set_up"></a>Set Up
------

Create your dev environment if you haven't already. This is how to do that.  

Clone the repo, enter the repo directory then create your virtual environment.  

For example:
```
git clone https://github.com/Azure/azure-cli.git
git clone https://github.com/Azure/azure-cli-extensions.git
python -m venv env
source env/bin/activate
azdev setup -c azure-cli -r azure-cli-extensions
```
For more information, see https://github.com/Azure/azure-cli-dev-tools#setting-up-your-development-environment.

After this, you should be able to run the CLI with `az`.

[Author your command module...](#heading_author_command_mod)

If your command module contributes any commands, they should appear when running `az`.
If your commands aren't showing with `az`, use `az --debug` to help debug. There could have been an exception
thrown whilst attempting to load your module.


<a name="heading_author_command_mod"></a>Authoring command modules
------

There are two options to initialize a command module:
1. Use [Azure CLI Code Generator tool](https://github.com/Azure/autorest.az#how-does-azure-cli-code-generator-work) to generate code automatically.
2. [Create a module with `azdev cli create`](https://azurecliprod.blob.core.windows.net/videos/04%20-%20AzdevCliCreate.mp4).

**Create an \_\_init__.py for your module**

In the \_\_init__ file, you will declare a command loader class that inherits from AzCommandsLoader. You will typically override the following three methods:
在 \_\_init__ 文件中，您将声明一个从 AzCommandsLoader 继承的命令加载器类。您通常会覆盖以下三个方法： 
  - `__init__` - Useful for setting metadata that applies to the entire module. For performance reasons, no heavy processing should be done here. See command authoring for more info.
  - `__init__` - 用于设置适用于整个模块的元数据。出于性能原因，此处不应进行繁重的处理。有关更多信息，请参阅命令创作。 
  - `load_commands_table` - Register command groups and commands here. It is common to store the implementation of this method in
                            a file named `commands.py` but for very small modules this may not be necessary. See command authoring for
                            more info.
  - `load_commands_table` - 在此处注册命令组和命令。通常将此方法的实现存储在名为“commands.py”的文件中，但对于非常小的模块，这可能没有必要。有关更多信息，请参阅命令创作。 
  - `load_arguments` - Apply metadata to your command arguments. It is common to store the implementation of this method in a file 
                       named `_params.py` but for very small modules this may not be necessary. See command authoring for more info.
  - `load_arguments` - 将元数据应用于您的命令参数。通常将此方法的实现存储在名为“_params.py”的文件中，但对于非常小的模块，这可能没有必要。有关更多信息，请参阅命令创作。

**__init__.py**
```Python
from azure.cli.core import AzCommandsLoader
from azure.cli.command_modules.mymod._help import helps  # pylint: disable=unused-import

class MyModCommandsLoader(AzCommandsLoader):

    def load_command_table(self, args):
      from azure.cli.core.commands import CliCommandType

      mymod_custom = CliCommandType(
        operations_tmpl='azure.mgmt.mymod.operations#MyModOperations.{}',
      )

      with self.command_group('myfoo', mymod_custom) as g:
        g.command('create', 'create_myfoo')

COMMAND_LOADER_CLS = MyModCommandsLoader
```

**custom.py**
```python
def create_myfoo(cmd, myfoo_name, resource_group_name, location=None):
    from azure.mgmt.example.models import MyFoo
    from azure.cli.command_modules.example._client_factory import cf_mymod
    client = cf_mymod(cmd.cli_ctx)

    foo = MyFoo(location=location)
    return client.create_or_update(myfoo_name, resource_group_name, foo)
```

The snippet above shows what it takes to author a basic command.
1. Create a CliCommandType which holds the metadata for your command. 
2. Create a command group in which your command will exist, passing the command type created in the previous step.
3. Register your command with the `command` method, defining first the name of the command and then the name of the method which will execute.
4. Define the callable that will execute:
    The CLI inspects the callable to determine required params, defaults and help text and more.  
    Try out the example to see these in action!

When running the command with the `--help` flag, you should see the command.
You can also now execute the command for yourself.

上面的代码片段显示了编写基本命令所需的条件。 
1. 创建一个 CliCommandType 来保存您的命令的元数据。 
2. 创建一个命令组，您的命令将在其中存在，传递上一步中创建的命令类型。 
3. 使用 `command` 方法注册您的命令，首先定义命令的名称，然后定义将执行的方法的名称。 
4. 定义将要执行的可调用对象：CLI 检查可调用对象以确定所需的参数、默认值和帮助文本等。试试这个例子，看看这些在行动！运行带有 `--help` 标志的命令时，您应该会看到该命令。您现在也可以自己执行命令。
```
$ az myfoo create --help

Command
    az myfoo create

Arguments
    --myfoo-name          [Required]: The argument that is required.
    --resource-group-name [Required]: Also required.
    --location                      : Optional arg.
...

$ az myfoo create --myfoo-name foo --resource-group-name myrg
{
  "name": "foo",
  "resourceGroup": "myrg",
  "location": None
}
```

Testing
-------

Discover tests

```
azdev test --discover
```

Run all tests in a module:

```
azdev test MODULE [--live] [--series] [--discover] [--dest-file FILENAME]
```

Run an individual test:

```
azdev test TEST [TEST ...] [--live] [--series] [--discover] [--dest-file FILENAME]
```
For example `azdev test test_myfoo`

Run a test when there is a conflict (for example, both 'azure-cli-core' and 'azure-cli-network' have 'test_foo'):
```
azdev test MODULE.TEST [--live]
```

The list of failed tests are displayed at the end of a run and dumped to the file specified with `--dest-file` or `test_failures.txt` if nothing is provided. This allows for conveniently replaying failed tests:
失败的测试列表在运行结束时显示并转储到用`--dest-file` 或`test_failures.txt` 指定的文件（如果没有提供）。这允许方便地重放失败的测试：

```
azdev test --src-file test_failures.txt [--live] [--series] [--discover]
```

Relying on the default filename, the list of failed tests should grow shorter as you fix the cause of the failures until there are no more failing tests.

Style Checks
------------

```
azdev style --module <module> [--pylint] [--pep8]
```

Submitting Pull Requests
------------------------

### Format PR Title

History notes are auto-generated based on PR titles and descriptions starting from [S165](https://github.com/Azure/azure-cli/milestone/82). Starting from 01/30/2020, we require all the PR titles to follow the below format:
历史记录是根据 PR 标题和从 [S165](https://github.com/Azure/azure-cli/milestone/82) 开始的描述自动生成的。从 01/30/2020 开始，我们要求所有 PR 标题遵循以下格式： 
1. [**Mandatory**] Each PR title **MUST** start with `[Component Name]` or `{Component Name}`. 
    * `Component Name` shall be replaced by the real ones such as `Storage`, `Compute`. It could be the name of a command module, but in title case with necessary spaces for better readability, such as `API Management`, `Managed Service`. Other possible component names include but are not limited to: `Packaging`, `Misc.`, `Aladdin`.
    * `[]` means this change is customer-facing and the message will be put into `HISTORY.rst`. `{}` means this change is not customer-facing and the message will **NOT** be included in `HISTORY.rst`.
    * If the component name is `Core`, the message will be written in `src/azure-cli-core/HISTORY.rst`. Otherwise, the message will be written in `src/azure-cli/HISTORY.rst`.
   [强制的] 每个 PR 标题必须以 `[Component Name]` 或 `{Component Name}` 开头。 `Component Name` 应替换为真实的，如`Storage`、`Compute`。
   它可能是一个命令模块的名称，但在标题的情况下，为了更好的可读性，需要有必要的空格，例如`API Management`、`Managed Service`。
   其他可能的组件名称包括但不限于：`Packaging`、`Misc.`、`Aladdin`。 
   `[]` 表示此更改是面向客户的，并且消息将放入 `HISTORY.rst`。 
   `{}` 表示此更改不是面向客户的，并且该消息不会包含在 `HISTORY.rst` 中。
   如果组件名称为`Core`，则消息将写入`src/azure-cli-core/HISTORY.rst`。
   否则，消息将写入`src/azure-cli/HISTORY.rst`。 
2. [**Mandatory**] If it's a breaking change, the second part should be `BREAKING CHANGE` followed by a colon. In the case of hotfix, put `Hotfix` in this part. If it's related to fixing an issue, put `Fix #number` in this part. For other cases, this part could be empty.
   [强制的] 如果是破坏性更改，第二部分应该是`BREAKING CHANGE` 后跟一个冒号。在hotfix的情况下，把`Hotfix`放在这部分。如果它与修复问题有关，请在此部分输入“修复编号”。对于其他情况，这部分可能是空的。 
3. [**Recommendation**] If the change can be mapped into a command, then the next part could be the command name starting with `az`, followed by a colon.
   [推荐] 如果改动可以映射成一个命令，那么下一部分可以是命令名以`az`开头，后跟一个冒号。 
4. [**Recommendation**] Use the right verb with **present-tense** in **base form** and **capitalized first letter** to describe what is done:
    * **Add** for new features.
    * **Change** for changes in existing functionality.
    * **Deprecate** for once-stable features removed in upcoming releases.
    * **Remove** for deprecated features removed in this release.
    * **Fix** for any bug fixes.
   [推荐] 使用正确的动词，基本形式的现在时和大写的第一个字母来描述所做的事情：
    * 添加新功能。
    * 更改现有功能的更改。
    * 弃用在即将发布的版本中删除的曾经稳定的功能。
    * 移除此版本中已移除的弃用功能。
    * 修复任何错误修复。

Examples of customer-facing change PR title:

> [Storage] BREAKING CHANGE: az storage remove: Remove --auth-mode argument  
> [ARM] Fix #10246: az resource tag crashes when the parameter --ids passed in is resource group ID
> az资源标签在传入参数--ids为资源组ID时崩溃

An example of non-customer-facing change PR title:

> {Aladdin} Add help example for dns

### Format PR Description

Please follow the instruction in the PR template to provide a description of the PR and the testing guide if possible. 

If you would like to write multiple history notes for one PR or overwrite the message in the PR title as a history note, please write the notes under `History Notes` section in the PR description, following the same format described above. The PR template already contains the history note template, just change it if needed. In this case, the PR title could be a summary of all the changes in this PR and will not be put into `HISTORY.rst` in our pipeline. The PR title still needs to start with `[Component Name]`. You can delete the `History Notes` section if not needed.
如果您想为一个 PR 编写多个历史注释或将 PR 标题中的消息覆盖为历史注释，请按照上述相同格式在 PR 描述的“历史注释”部分下编写注释。 PR 模板已包含历史记录模板，只需根据需要更改即可。在这种情况下，PR 标题可能是此 PR 中所有更改的摘要，不会放入我们管道中的“HISTORY.rst”。 PR 标题仍然需要以 `[Component Name]` 开头。如果不需要，您可以删除“历史记录”部分。

### Hotfix PR
Step 1: Create a hotfix branch based on `release` branch, then submit a PR to merge the hotfix branch into `release`.

In this PR, the second part of the PR title should be `Hotfix`. If you have customer-facing changes, you need to manually modify `HISTORY.rst` to add history notes. The auto-generated history notes for the next regular release will ignore the PR that contains `Hotfix`.

An example title of hotfix change PR:

> {Packaging} Hotfix: Fix dependency error

Step 2: After the hotfix version is released, submit a PR to merge `release` branch back to `dev` (e.g. [#15505](https://github.com/Azure/azure-cli/pull/15505)).

⚠ Do **NOT** squash merge this PR. After the PR gets approved by code owners, merge `release` to `dev` by creating a **merge commit** on your local machine, then push `dev` to upstream repository. The PR will automatically be marked as **Merged**.
不要挤压合并这个 PR。在 PR 获得代码所有者的批准后，通过在本地机器上创建合并提交将 `release` 合并到 `dev`，然后将 `dev` 推送到上游存储库。 PR 将自动标记为已合并。
