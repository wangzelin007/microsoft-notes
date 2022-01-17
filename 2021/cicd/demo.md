I'll take control.
I just start sharing. Let me know if you can see my screen.
Hello everyone, Happy new year!
Today I'm gonna to share you with the demo of azure cli command coverage.
This feature will allow azure CLI dev tools auto generate CLI Command Coverage Report about every module to track and improve code quality.
And the linter will add two rules to detect any missing test cases in every pull request.
After the linter failed, The CLI CI pipeline will notify developer to add missing test.
So we can continuously improve code quality in every pull request.
We support two level command coverage report, one is command level, the other is argument level.
You can click the table head to sort the table data and switch to show all modules or cli own modules.
I want to Thanks my team, we can see with their help the coverage of cli own modules has exceeded 93%.
For each module, we can check which commands and parameters have not been tested.
For scenarios that cannot be tested, 
for example: To comply with security compliance, we can not test dash dash password.
and some scenarios require many preconditions, 
We can choose modules or commands or arguments to exclude.
And we add two new rules for linter to check in every pull request.
one is Missing Command Coverage, the other is Missing Argument Coverage.
Corresponding to the two levels of Command Coverage Report.
We will compare the source branch with our main branch, then search for the new commands and arguments add in this pull request 
(through a series of regular expressions).
The next step we will find out whether the PR contain the required test code.
For special cases where tests cannot be provided, we also support add rule exclusion to the original linter exclusion yaml file to skip checking.
I've prepared a small demo for a quick demonstration.
Let me check out to the demo branch
`git co cmdcov-demo-pre`
For example, this developer add two new commands and two new arguments, but not write any test.
Let's run the linter check. 
`azdev linter --rule-types command_coverage --ci-exclusions  --repo=C:\code\azure-cli --src=cmdcov-demo-pre --tgt=dev`
Now we can see, all missing test commands and arguments were detected by the linter.
Let me check out to another branch that I write all the test.
`git co cmdcov-demo-post`
Let's run the linter check again.
`azdev linter --rule-types command_coverage --ci-exclusions  --repo=C:\code\azure-cli --src=cmdcov-demo-post --tgt=dev`
Now we can see, the command coverage linter rule is passed. 
Let me check out to third branch that I skip all the commands and argumemts.
`git co cmdcov-demo-skip`
And run the linter check again.
`azdev linter --rule-types command_coverage --ci-exclusions  --repo=C:\code\azure-cli --src=cmdcov-demo-skip --tgt=dev`
Now we can see, the command coverage linter rule is also passed because of exclusion. 

And in the next version we have some Future requirements:
1. To support azure cli extensions
2. To create a pipeline to run cli command coverage report once a week and save all the data to blob and database.
3. To use these data to track and display the trend of cli command coverage.

So that's all for my demo, Thank you.

azdev 解释
1. pipeline
2. 原因分类