I'll take control.
I just start sharing. Let me know if you can see my screen.
Hello everyone!
Today I'm going to share you with the demo of Azure CLI automated testing speed up.

A year ago, we started the initiative(x) in Azure Core to build a strong culture of quality. Quality is the most important aspect(x) of our work as customers trust us to support their critical workloads on Azure. 
So our team decides to increase our test coverage: Add test is an excellent(x) way to improve quality and is now a ubiquitous(x) practice. 
So we add a new feature to allow azure CLI dev tools auto-generate CLI Command Test Coverage Report about every module.

But with more and more tests being added.
Our automated testing is getting slower.
This picture is pipeline duration report from the azure devops portal
We can see now it will take more than 70 minutes to run automated testing after a pull request.

I use three s`teps to gradually increase the test speed.
Our first step is to add a new parameter "--durations" to record the time spent on each test.
And according to the test duration, I fix the top N slowest tests one by one.
It can totally save more than 20 minutes.
After this step, the test time is reduced to about 50 minutes

Then I enable group worker in our test framework, it will spawn(x) a number of worker processes(x) equal to the number of available CPUs(x), and distribute the tests randomly(x) across them.
Why not enable more group workers ?
When more workers are enabled, the generation and switching of workers also have additional overhead, which will lead to slower testing speed.
After this step, the test time is reduced to about 30 minutes

I found that we run all the tests in one pipeline instance.
But we share the VM pool with the azure-SDK team, and the azure-SDK team has 50 total machines.
So I split automated testing to 8 pipeline instances
And we have 3 python versions need to support.
So we use a total of 24 machines to test at the same time.
If you add more instances, the pipeline will occupy a large percentage of this allocation at once which starved other pipelines from being able to get any instance, and the actual execution time will be longer.

Now we have 71 modules being tested in one instance.
If we use the multi-instance(x) test, we need automatic scheduling 71 modules in 8 pipeline instance
So I write a greedy algorithm(x) to distribute modules to each instance
For example, let's say we have 10 modules and 2 pipeline instances.
For each module, we record their historical(x) execution time and then sort by descending(x) order.
Then we assign the module to an instance with the fewest job duration currently to ensure the execution time of each pipeline instance is close to each other
For the newly added module we can use module average test time.
After this step, the test time is reduced to about 10 minutes
Our automated testing pipeline duration has been reduced by over 80 percent.

At last, I would like to thank my team, we have a brainstorming on how to speed up automated testing.
That's why we have three steps

So that's all for my demo, Thank you.

如何修复测试的：
We mainly fixed two types of issues.
1. If the list command shows too many resources, we only check the correctness of the first resource through the show command instead of looping through all the resources.
2. Mock all time.sleep methods in automated testing. Because except for live test, we don't need long wait.

迁移的影响：
If we migrate to 1ES Pool, we don't need to modify our pipeline.
We just need to re-specify the pool from sdk pool to 1ES pool

改进表格：Done
贪心算法动图：Done
learning：
支撑别的team：Done
欢迎联系。

