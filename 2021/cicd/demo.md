I'll take control.
I just start sharing. Let me know if you can see my screen.
Hello everyone, Happy new year!
Today I'm gonna to share you with the demo of azure cli command test coverage.
Previously, we have no way to check the test coverage of Azure CLI, 
and we must manually check every pull request, to ensure all test cases was added.
From now this feature will allow azure CLI dev tools auto generate CLI Command Test Coverage Report about every module.
And detect any missing test cases in every pull request.
So we can continuously track and improve code quality and save a lot of time.

As you can see we support two level command test coverage report, one is command level, the other is argument level.
You can click the table head to sort the table data and switch to show all modules or cli own modules.
I want to thank my team, we can see with their help the coverage of cli own modules has exceeded 97%.
I leave an Easter egg here, only test coverage exceed 100% will show a gold medal.
For each module, we can check which commands and parameters have not been tested.
For scenarios that cannot be tested, 
For example: we can not test dash dash password as this would expose our password information
or some scenarios require some preconditions that is difficult to prepare.
We can choose modules or commands or arguments to exclude.
That's all for the test coverage report

And we add two new rules for linter to check in every pull request.
one is Missing Command Test Coverage, the other is Missing Argument Test Coverage.
Corresponding to the two levels of Command Test Coverage Report.
The command test coverage pipeline will trigger by every pull request.
Then we will compare the source branch with our main branch, then search for the new commands and arguments add in this pull request
The next step we will find out whether the pull request contain the required test code.
For special cases where tests cannot be provided, we also support add rule exclusion to the original linter exclusion yaml file to skip checking.
I have prepared a small demo for a quick demonstration.

For example, In this draf pull request I add some new commands and arguments, but not write any test in this pull request.
Because in this scenario we assume that sdk is not publish, so we can not add test.
Now we can see, CLI Command Test Coverage Check is failed, all missing test commands and arguments were detected by the check.
So this will force everyone to add test to pass these checks and merge into our main branch.

In the second pull request demo, we add the scenario test, so command test coverage check is passed.

If we cannot add test because of some reason, we need add exclusion in the linter exclusion file
In the third pull request demo,although we don't test any commands, but we add them to the exclusion file,
The cli command test coverage check is also passed. 

And in the next version we will implement some new features:
1. To support azure cli extension repo.
2. To save all cli command test coverage report data to database and blob.
3. To use these data to track and display the trend of cli command test coverage and display some beautiful chart in Power BI.

So that's all for my demo, Thank you.
