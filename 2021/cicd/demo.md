I'll take control.
I just start sharing. Let me know if you can see my screen.
Hello everyone, Happy new year and may the New Year bring many good things and rich blessings to you and all those you love!
Today I'm gonna to share you with the demo of azure cli command coverage.
以前CLI没有command coverage, 所以我们需要在review pr时仔细检查是否包含对应的场景测试。整个过程都是人工的，会耗费大量的时间。
即便如此还是会漏掉一些测试，而且我们无法得知所有模块的测试情况。
So this feature will allow azure CLI dev tool auto generate CLI Command Coverage Report about every module to track and improve test coverage.
And the linter will add two rules to detect any missing test cases in every pull request, so we can continuously improve code quality.
我们支持两种级别的command coverage，一种是command级别，一种是argument level.
We support two level commmand coverage， one is command level report, the other is argument level.
我们可以对每个字段进行排序，同时我们可以快速查看所有 cli team own 的 modules.
You can click the table head to sort the table data and switch to show all modules or cli own modules.
对于每个module，我们都可以点击来查看具体哪些命令和参数没有被测试过。
For each module， we can check which commands and parameters have not been tested.
同时对于无法测试的场景，比如： 需要提供用户名，密码 等涉及到安全合规的场景， 以及需要很多前置条件的场景， 我们支持按照module， command， argument 进行过滤。
At the same time, for scenarios that cannot be tested, such as: user names, passwords, etc. that involve security compliance, and scenarios that require many preconditions, we support filtering by module, command, and argument.
同时为了持续改进command coverage，我们对linter新增了两种rule
And we add two new rules for linter to check in every pull request.
一个是 Missing Command Coverage， 一个是 Missing Argument Coverage.
one is Missing Command Coverage, the other is Missing Argument Coverage.
分别对应了两种级别的 Command Coverage Report.
Corresponding to two levels of Command Coverage Report.
我们会对比每次提交代码的分支和我们的主干分支，然后通过一系列的正则表达式，搜索出本次PR新增的 command 和 argument。
We will compare the branch of each submitted code with our main branch, and then search for the new command and argument of this PR through a series of regular expressions.
然后再查找PR是否完善了相关的测试用例。以此来确保所有PR都包含了需要的测试代码。
Then find out whether the PR has improved the relevant test cases. This ensures that all PRs contain the required test code.
对于无法提供测试的特殊情况，我们也支持在原有的 linter_exclusions.yml 文件中添加 rule_exclusion 来跳过检查。
For special cases where tests cannot be provided, we also support adding rule_exclusion to the original linter_exclusions.yml file to skip checking.
我准备了一个小demo，可以快速展示一下。
I've prepared a small demo for a quick demonstration.
比如这个用户的新增了两个command 和 两个 argument，但是没有写任何测试用例。
For example, this developer add two new commands and two arguments, but did not write any test cases.
现在我们运行一下新的linter check。
Let's run a the linter check. `linter --rule-types command_coverage --ci-exclusions  --repo=D:\code\azure-cli --src=20141 --tgt=dev`
可以看到，我们检测出了所有缺失测试的command 和 argument。
Now we can see, all missing test commands and arguments were detected by the linter.
So that's all for my demo, Thank you.
