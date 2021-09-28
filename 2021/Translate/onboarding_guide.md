Onboarding Best Practices
=========================

As a prerequisite, please contact Carl Shipley first for the [PLR](http://aka.ms/plrcriteria) (Product Launch Readiness) process.
作为先决条件，请先联系 Carl Shipley 以进行 [PLR](http:aka.msplrcriteria)（产品发布准备）流程。
Then reach out to `azpycli@microsoft.com` to get the CLI onboarding process started. You'll be assigned a dev contact on the CLI team. Early and frequent communication with this contact is essential to ensuring a smooth onboarding.
然后联系 `azpycli@microsoft.com` 以启动 CLI 入门流程。您将被分配到 CLI 团队的开发联系人。与此联系人的早期和频繁沟通对于确保顺利入职至关重要。

## Extension vs. Module

One of the key decisions you will need to make is whether to create your commands in a CLI module or an extension.

#### Extensions

|                      PROS                      |                         CONS                         |
|:----------------------------------------------:|:----------------------------------------------------:|
| Release separate from the CLI release schedule | Requires dedicated installation (az extension add …) |
| Higher velocity fixes possible                 | Can be broken by changes to the azure-cli-core       |
| Experimental UX is permissible                 |                                                      |
| Leverage CLI code generator to generate code   |                                                      |
|优点 |缺点 | 
|:----------------------------------------------:| :------------------------------------------------- ---:| 
|与 CLI 发布计划分开发布 |需要专用安装（az 扩展添加...） | 
|更高的速度修复可能|可以通过更改 azure-cli-core 来破坏 | 
|实验性用户体验是允许的 | | 
|利用 CLI 代码生成器生成代码 | |

#### CLI Modules

|                                   PROS                                  |                                                                             CONS                                                                             |
|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Comes automatically with the CLI. No dedicated installation required.   | Strictly tied to CLI release schedule                                                                                                                        |
| Unlikely to be broken by changes to azure-cli-core (with test coverage) | STRICTLY tied to CLI authoring guidelines. Experimental patterns that may be allowed in extensions could be rejected entirely for inclusion as a CLI module. |
|优点 |缺点 | 
|:------------------------------------------------ ---------------:|:------------------------ -------------------------------------------------- -------------------------------------------------- --------------------------------:| 
|随 CLI 自动提供。无需专门安装。 |严格绑定到 CLI 发布时间表 | 
|不太可能被 azure-cli-core 的改变破坏（有测试覆盖）|严格绑定到 CLI 创作指南。扩展中可能允许的实验模式在CLI 模块中可能会被完全拒绝。 |

- Common uses for extensions include experimental commands, commands in private or public preview, or to separate between frequently used and rarely used functionality (where infrequently used commands are acquired via extension).
- 扩展的常见用途包括实验性命令、私人或公共预览中的命令，或将常用和很少使用的功能（其中不常用的命令通过扩展获取）分开。 - 请注意，如果您尝试将命令输入 CLI 与正常发布周期不一致，则扩展是您唯一的选择。
- Note that if you are trying to get commands into the CLI out of step with the normal release cycle, extensions are your **only** option.
- 请注意，如果您尝试将命令输入 CLI 与正常发布周期不一致，则扩展是您唯一的选择。
- Because non-standard, experimental authoring patterns are permitted for extensions, simply trying to "move an extension into the CLI" is often **not** a trivial process and will necessitate a full review with higher scrutiny from the CLI team. Expect to need to make changes.
- 因为扩展允许使用非标准的、实验性的创作模式，所以简单地尝试“将扩展移动到 CLI”通常不是一个简单的过程，并且需要 CLI 团队进行更严格审查的全面审查。预计需要进行更改。
- If you want to use CLI code generator to generate CLI code automatically, extension is your **only** option. Please reference [AZ CLI Codegen On boarding](https://github.com/Azure/autorest.az/blob/master/doc/00-onboarding-guide.md) and start from **Step 2** now.
- 如果您想使用 CLI 代码生成器自动生成 CLI 代码，扩展是您唯一的选择。请参考 [AZ CLI Codegen On boarding](https:github.comAzureautorest.azblobmasterdoc00-onboarding-guide.md) 并立即从第 2 步开始。

## Initial Timeline and Milestones
初始时间表和里程碑

- **Initial Kickoff:** Reach out to your contact on the CLI team. Set up a short 30 minute Teams call to discuss initial questions.
- 初始启动：联系您在 CLI 团队中的联系人。设置一个 30 分钟的团队电话会议来讨论最初的问题。 
- **Initial Review:** Create a few commands. Schedule a short 30 minute Teams screen-share to demo your commands. This is crucial! Teams have created entire modules using anti-patterns, resulting in comment-filled PRs and last-minute rework! A quick command review would have prevented this.
- 初步审查：创建一些命令。安排一个 30 分钟的 Teams 屏幕共享来演示您的命令。这很关键！团队使用反模式创建了整个模块，从而产生了充满评论的 PR 和最后一刻的返工！快速的命令审查可以防止这种情况发生。
- **During command authoring:** Run checks frequently to ensure you are staying on top of issues that will stall your build when you submit a PR. Use commands like `azdev test <YOURMOD>`, `azdev style <YOURMOD>` and `azdev linter <YOURMOD>`.
- 在命令创作期间：经常运行检查，以确保您在提交 PR 时能及时处理会导致构建停滞的问题。使用诸如 `azdev test <YOURMOD>`、`azdev style <YOURMOD>` 和 `azdev linter <YOURMOD>` 之类的命令。 
- **Periodic Command Review:** As practical.
- 定期命令审查：切实可行。 
- **Just before opening PR:** Run `azdev style` and `azdev linter --ci-exclusions` and `azdev test <YOURMOD>` to address issues before the CI finds them.
- 在打开 PR 之前：运行 `azdev style` 和 `azdev linter --ci-exclusions` 和 `azdev test <YOURMOD>` 以在 CI 发现问题之前解决问题。 
- **2 weeks before desired release date:** Open PR in CLI repo (public or private depending on your service). Request your CLI contact as the reviewer for the PR.
- 期望发布日期前 2 周：在 CLI 存储库中打开 PR（公共或私有，取决于您的服务）。请求您的 CLI 联系人作为 PR 的审阅者。 
- **1 week prior to desired release date:** Hopefully, PR is merged! Download the edge build and try it out. Submit follow-up PRs to address any small issues. Anything caught before release is not a breaking change!
- 期望发布日期前 1 周：希望 PR 已合并！下载边缘版本并尝试一下。提交后续 PR 以解决任何小问题。在发布之前捕获的任何内容都不是破坏性更改！

## Initial Pull Request Guidance
初始拉取请求指南

Reviewing a new command module is very difficult, so the PR shouldn't be the first time we see your module! Some important considerations for your initial PR:
审查一个新的命令模块非常困难，所以 PR 不应该是我们第一次看到你的模块！初始 PR 的一些重要考虑事项： 
1. Have recorded ScenarioTests for **all** new commands. This lets us know that your commands *work*. [Test Authoring](https://github.com/Azure/azure-cli/blob/dev/doc/authoring_tests.md)
已记录所有新命令的 情景测试。这让我们知道您的命令有效。 [Test Authoring](https:github.comAzureazure-cliblobdevdocauthoring_tests.md) 
2. If you are creating brand new commands, they should be marked as being in Preview. See: [Preview Commands and Arguments](https://github.com/Azure/azure-cli/blob/dev/doc/authoring_command_modules/authoring_commands.md#preview-commands-and-arguments)
如果您正在创建全新的命令，应将它们标记为处于预览状态。请参阅：[预览命令和参数](https:github.comAzureazure-cliblobdevdocauthoring_command_modulesauthoring_commands.mdpreview-commands-and-arguments) 
3. (OPTIONAL) The help output of:
   - all groups and subgroups (i.e. `az vm -h`)
   - all non-trivial commands (commands except `list`, `show`, `delete`)
（可选）帮助输出： 
   - 所有组和子组（即`az vm -h`） 
   - 所有重要的命令（除了 `list`、`show`、`delete` 之外的命令）

If you and your CLI contact have been doing regular command reviews, the PR should merely be a formality. If you haven't been conducting regular reviews, the help output allows us to quickly identify holes and anti-patterns to get you on the right track.
如果你和你的 CLI 联系人一直在做定期的命令审查，那么 PR 应该只是一种形式。如果您没有进行定期审查，帮助输出使我们能够快速识别漏洞和反模式，让您走上正轨。
The help output is generally not needed if a command walkthrough has been conducted, but is often a helpful alternative for teams who are in a very different time zone such that scheduling a live review would be highly inconvenient.
如果执行了命令演练，通常不需要帮助输出，但对于处于非常不同时区的团队来说，帮助输出通常是一个有用的替代方案，因此安排实时审查会非常不方便。

## Transition Paths
过渡路径 
Nearly all new command modules or extensions begin life in Preview, but will eventually want to transition to being GA. The section describes the review requirements required for various transitions.
几乎所有新的命令模块或扩展都在预览版中开始使用，但最终都希望过渡到 GA。本节描述了各种转换所需的审查要求。

#### Preview Extension to GA Extension

This is the easiest to accomplish.
这是最容易实现的。 

- Underlying service must be GA.
- 基础服务必须是 GA。 
- Existing command UX must be stable.
- 现有的命令 UX 必须稳定。 todo 什么是UX
- Author must acknowledge they will no longer be able to simply make breaking changes but will instead need to follow [deprecation mechanisms](https://github.com/Azure/azure-cli/blob/dev/doc/authoring_command_modules/authoring_commands.md#deprecating-commands-and-arguments).
- 作者必须承认他们将不再能够简单地进行重大更改，而是需要遵循 [弃用机制]（https:github.comAzureazure-cliblobdevdocauthoring_command_modulesauthoring_commands.mddeprecating-commands-and-arguments）。


#### Preview Extension to Preview Module

Because extensions are permitted to try experimental things that may be antithetical to the CLI's conventions, it is not automatic that a preview extension can just transition to being a preview module.
由于允许扩展尝试与 CLI 约定背道而驰的实验性事物，因此预览扩展不能自动转换为预览模块。 

- Command review required.
- 需要命令审查。 
- Commands must conform to CLI standards and may no longer be permitted to do experimental things that they previously could as an extension.
- 命令必须符合 CLI 标准，并且可能不再被允许执行以前可以作为扩展的实验性操作。

#### Preview Extension/Module to GA Module

This is a significant transition for any service.
这对任何服务来说都是一个重要的过渡。 
- Underlying service must be GA.
- 基础服务必须是 GA。 
- Command review required.
- 需要命令审查。 
- Command UX must be stable for several releases and conform to CLI standards.
- 命令 UX 必须在多个版本中保持稳定并符合 CLI 标准。 
- No deficiencies permitted which would necessitate future breaking changes. Instead, the breaking changes should be made as part of a preview release and allowed to stabilize.
- 不允许存在需要未来重大更改的缺陷。相反，重大更改应作为预览版本的一部分进行并使其稳定。 
- Minor deficiencies which can be fixed through additive, non-breaking changes are permissible (for example, missing argument completers or missing generic update arguments).
- 可以通过附加的、不间断的更改来修复的小缺陷是允许的（例如，缺少参数完成器或缺少通用更新参数）。 
- Author must acknowledge they will no longer be able to simply make breaking changes but will instead need to follow [deprecation mechanisms](https://github.com/Azure/azure-cli/blob/dev/doc/authoring_command_modules/authoring_commands.md#deprecating-commands-and-arguments).
- 作者必须承认他们将不再能够简单地进行重大更改，而是需要遵循 [弃用机制]（https:github.comAzureazure-cliblobdevdocauthoring_command_modulesauthoring_commands.mddeprecating-commands-and-arguments）。

#### GA Extension to GA Module

Because extensions are permitted to try experimental things that may be antithetical to the CLI's conventions, no benefit is afforded a GA extension in trying to become a module. In reality, the fact that the extension is GA can actually be more of a hindrance because any breaking changes that may be necessitated to conform with CLI standards will need to go through [deprecation mechanisms](https://github.com/Azure/azure-cli/blob/dev/doc/authoring_command_modules/.
因为扩展被允许尝试可能与 CLI 约定背道而驰的实验性事物，所以在尝试成为模块时，GA 扩展没有任何好处。实际上，扩展是 GA 的事实实际上可能是更多的障碍，因为任何可能需要符合 CLI 标准的破坏性更改都需要通过 [弃用机制](https:github.comAzureazure-cliblobdevdocauthoring_command_modules。

- Command review required.
-命令需要审查。 
- Commands must conform to CLI standards and may no longer be permitted to do experimental things that they previously could as an extension. This could necessitate breaking changes which will need to be accomplished using
[deprecation mechanisms](https://github.com/Azure/azure-cli/blob/dev/doc/authoring_command_modules/authoring_commands.md#deprecating-commands-and-arguments).
- 命令必须符合 CLI 标准，并且可能不再被允许做他们以前可以作为扩展的实验性事情。这可能需要使用 [deprecation mechanisms](https://github.com/Azure/azure-cli/blob/dev/doc/authoring_command_modules/authoring_commands.md#deprecating-commands-and-arguments). 
- Minor deficiencies which can be fixed through additive, non-breaking changes are permissible (for example, missing argument completers or missing generic update arguments).
- 允许通过附加的非破坏性更改修复的小缺陷（例如，缺少参数完成程序或缺少通用更新参数）。
