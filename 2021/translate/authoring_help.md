# Azure CLI Help System

Help authoring for commands is done in a number of places, all of which are contained in the Az code base.  Some help text comes from product code, but it can be overridden using a YAML-based help authoring system.  The YAML-based system is the recommended way to update command and group help text.
命令的帮助创作在许多地方完成，所有这些都包含在 Az 代码库中。一些帮助文本来自产品代码，但可以使用基于 YAML 的帮助创作系统覆盖它。基于 YAML 的系统是更新命令和组帮助文本的推荐方式。

## YAML Help Authoring

If you're not familiar with YAML, see the [YAML specification](http://www.yaml.org/spec/1.2/spec.html).

To override help for a given command:

1. Find the command's module, Example "az account clear".
	1. Search code base for "account clear".
	2. Search result: src/command_modules/azure-cli-**profile**/azure/cli/command_modules/**profile**/commands.py.
	3. Result shows "account clear" is in the "profile" module.
2. Using the module name, find the YAML help file which follows the path pattern.:
	1.  src/command_modules/azure-cli-**[module name]**/azure/cli/command_modules/**[module name]**/_help.py<br>
	    **or** <br>
	    src/command_modules/azure-cli-**[module name]**/azure/cli/command_modules/**[module name]**/help.yaml
	2.  If the file doesn't exist, it can be created.
3.  Find or create a help entry with the name of the command/group you want to document.  See example below.


>  ###Notes: <br>
>  1. If using **_help.py** files for help authoring, the command module's **\_\_init\_\_.py** file must import the **_help.py** file. i.e: <br>
>    `import azure.cli.command_modules.examplemod._help` <br>
>  2. The Help Authoring System now supports **help.yaml** files. Eventually, **_help.py** files will be replaced by **help.yaml**.


### Example YAML help file, \_help.py

```python
#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------

from knack.help_files import helps

#pylint: disable=line-too-long

helps['account clear'] = """
type: command
short-summary: Clear account
long-summary: Longer summary of clearing account
parameters: 
    - name: --account-name -n
      type: string
      short-summary: 'Account name'
      long-summary: |
          Longer summary with newlines preserved.  Preserving newlines is helpful for paragraph breaks.
          保留换行符的更长摘要。保留换行符有助于分段。
      populator-commands: 
        - az account list
    - name: --another-parameter
      short-summary: These parameter names must match what is shown in the command's CLI help output, including abbreviation.
examples:
    - name: Collapse whitespace in YAML
      text: >
        The > character collapses multiple lines into a single line, which is good for on-screen wrapping.
"""
```

You can also document groups using the same format.

```python
helps['account'] = """
type: group
short-summary: The account group
long-summary: Longer summary of account            
examples:
    - name: Clear an account 
      text: Description
    - name: Choose your current account
      text: az account set...
"""
```

# Tips to write effective help for your command
为您的命令编写有效帮助的提示

- Make sure the doc contains all the details that someone unfamiliar with the API needs to use the command.
- 确保文档包含不熟悉 API 的人使用该命令所需的所有详细信息。
- Examples are worth a thousand words. Provide examples that cover common use cases.
- 例子值一千字。提供涵盖常见用例的示例。
- Don't use "etc". Sometimes it makes sense to spell out a list completely. Sometimes it works to say "like ..." instead of "..., etc".
- 不要使用“等”。有时，完整地列出一个列表是有意义的。大多数时候“喜欢……”比“……等”更有效。
- Use active voice. For example, say "Update web app configurations" instead of "Updates web app configurations" or "Updating web app configurations".
- 使用主动语态。例如，说“Update web app configurations”而不是“Updates web app configurations”或“Updating web app configurations”。
- Don't use highly formal language. If you imagine that another dev sat down with you and you were telling him what he needs to know to use the command, that's exactly what you need to write, in those words.
- 不要使用高度正式的语言。如果你想象另一个开发人员和你坐下来，你正在告诉他他需要知道什么才能使用这些命令，这正是你需要写的，用那些话。
- If the help message contains **angle brackets**, like `<name>`, it will be parsed as an HTML tag during document rendering. To bypass that, quote the content with backticks `` `<name>` `` to tell the document renderer to parse it as **code**. 
- 如果帮助消息包含尖括号，例如 `<name>`，它将在文档呈现期间被解析为 HTML 标记。要绕过它，请使用反引号 `` `<name>` `` 引用内容，以告诉文档渲染器将其解析为代码。

# Testing Authored Help
测试编写的帮助

To verify the YAML help is correctly formatted, the command/group's help command must be executed at runtime.  For example, to verify "az account clear", run the command "az account clear -h" and verify the text.  
要验证 YAML 帮助的格式是否正确，必须在运行时执行命令组的帮助命令。例如，要验证“az account clear”，请运行命令“az account clear -h”并验证文本。

Runtime is also when help authoring errors will be reported, such as documenting a parameter that doesn't exist.  Errors will only show when the Azure CLI help is executed, so verifying the Azure CLI help is required to ensure your authoring is correct.
运行时也会报告帮助创作错误，例如记录不存在的参数。错误只会在执行 Azure CLI 帮助时显示，因此需要验证 Azure CLI help以确保您的创作正确无误。

# Other Help Authoring

Commands without YAML usually still have help text.  Where does it come from?  These sections briefly outline where Az help text comes from.
没有 YAML 的命令通常仍然有帮助文本。它从何而来？这些部分简要概述了 Az 帮助文本的来源。

Authoring note: it is not recommended to use the product code to author command/group help--YAML is the recommended way (see above).  This information is provided for completeness and may be useful for fixing small typos in existing help text.
编写说明：不建议使用产品代码编写命令组帮助——推荐使用 YAML 方式（见上文）。提供此信息是为了完整性，可能有助于修复现有帮助文本中的小错别字。

## Help Layers

Command help starts with its raw SDK docstring text, if available.  Non-SDK commands may have their own docstring.  Code can specify values that replace the SDK/docstring contents.  YAML is the final override for help content and is the recommended way for authoring command and group help.  Note that group help can only be authored via YAML.  
命令帮助以其原始 SDK 文档字符串文本开头（如果可用）。非 SDK 命令可能有自己的文档字符串。代码可以指定替换 SDKdocstring 内容的值。 YAML 是帮助内容的最终覆盖，并且是编写命令和组帮助的推荐方式。请注意，组帮助只能通过 YAML 创作。

Here are the layers of Project Az help, with each layer overriding the layer below it:
以下是 Project Az 帮助的图层，每个图层都覆盖其下方的图层：

| Help Display                  |
|-------------------------------|
| YAML Authoring via *_help.py* |
| Code Specified                |
| Docstring                     |
| SDK Text                      |

## Page titles for command groups
命令组的页面标题

Page titles for your command groups as generated from the source are simply the command syntax, "az vm", but we use friendly titles on the published pages - "Virtual machines - az vm". To do that, ee add the friendly part of the page title to [titlemapping.json](https://github.com/Azure/azure-docs-cli/blob/master/titleMapping.json) in the azure-docs-cli repo. When you add a new command group, make sure to update the mapping.
从源代码生成的命令组的页面标题只是命令语法“az vm”，但我们在发布的页面上使用友好的标题 - “Virtual machines - az vm”。为此，ee 将页面标题的友好部分添加到 azure-docs-cli repo 中的 [titlemapping.json](https:github.comAzureazure-docs-cliblobmastertitleMapping.json)。添加新命令组时，请确保更新映射。

## Profile specific help
个人资料特定帮助

The Azure CLI supports multiple profiles. Help can be authored to take advantage of this.  
Commands available, arguments, descriptions and examples all change dynamically based on the profile in use.
Azure CLI 支持多个配置文件。可以编写帮助以利用这一点。可用命令、参数、描述和示例都根据使用的配置文件动态更改。

The `az cloud update --profile ...` command allows you to switch profiles.  
You can see an example of this by switching profiles and running `az storage account create --help`.

---

Below is some documentation on taking advantage of this in your YAML help files.

In your YAML files, the same `short-summary` and `long-summary` is used for all profiles.

For the command parameters section, any parameters not used by a profile will be ignored and not displayed.

For command examples, you can optionally specify the profile the example is for with the `supported-profiles` and `unsupported-profiles` fields.
对于命令示例，您可以选择使用 `supported-profiles` 和 `unsupported-profiles` 字段指定示例的配置文件。

Here's a demonstration for `storage account create`:
The first example is only supported on the `latest` and `2018-03-01-hybrid` profiles whilst the second example is only supported on `2017-03-09-profile`.

### \_help.py

```console
    examples:
        - name: Create a storage account MyStorageAccount in resource group MyResourceGroup in the West US region with locally redundant storage.
          text: az storage account create -n MyStorageAccount -g MyResourceGroup -l westus --sku Standard_LRS
          unsupported-profiles: 2017-03-09-profile 指定式
          # alternatively 或者
          # supported-profiles: latest, 2018-03-01-hybrid
        - name: Create a storage account MyStorageAccount in resource group MyResourceGroup in the West US region with locally redundant storage.
          text: az storage account create -n MyStorageAccount -g MyResourceGroup -l westus --account-type Standard_LRS
          supported-profiles: 2017-03-09-profile 指定式
```

Here is how this looks in Azure CLI `--help`:

On profiles `latest` and `2018-03-01-hybrid`.

```console
Examples
    Create a storage account MyStorageAccount in resource group MyResourceGroup in the West US
    region with locally redundant storage.
        az storage account create -n MyStorageAccount -g MyResourceGroup -l westus --sku
        Standard_LRS
```

On profile `2017-03-09-profile`.

```console
Examples
    Create a storage account MyStorageAccount in resource group MyResourceGroup in the West US
    region with locally redundant storage.
        az storage account create -n MyStorageAccount -g MyResourceGroup -l westus --account-type
        Standard_LRS
```

## Online Reference Documentation
在线参考文档

The help that you author above will be available online as reference documentation.
您在上面编写的帮助将作为参考文档在线提供。

https://docs.microsoft.com/cli/azure/reference-index

If you are not satisfied with the heading that is automatically provided, please create a PR to update the following file:
如果您对自动提供的标题不满意，请创建 PR 以更新以下文件：
PR：Pull Request

https://github.com/Azure/azure-docs-cli/blob/master/titleMapping.json
