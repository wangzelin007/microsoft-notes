Good morning Ben, my name is Zelin Wang. I am 31 years old.
I have graduated from the Nanjing University of Posts and Telecommunications.
I am from China, and now I am living in Shanghai.
I was a developer of ping an Cloud before I join Microsoft.
In pagan, I was mainly responsible for the automated installation and deployment of the network service platform.
I set up the CICD process in our department.
I am also involved in the development of nat gateway and load-balance.

After joining Microsoft,
My manager YongZhang signed me up for azure Bootcamp.
In Bootcamp I learned how to use Azure cloud and related development tools
And my tutor is YuChen, He helped me quickly get started with Azure CLI development
And all my colleagues are very nice. Whenever I ask a question, they answer quickly.
In the first two months, I was mainly involved in the development of some simple requirements for network and compute.

Because I have CICD(continuous integration and continuous deployment) related work experience.
So I developed a tool to auto-generate CLI Command Test Coverage Report about every module.
We support two-level command test coverage reports, one is command level, and the other is argument level.
And I add new rules for linter to check in every pull request.
The new rules will trigger every pull request, and it can find out whether the pull request contains the required test code.
And with this tool, the test coverage of CLI own modules has exceeded 97%.
I already demonstrated this feature in the sprint review meeting.
(We will compare the source branch with our main branch, then search for the new commands and arguments add to this pull request
Then we will find out whether the pull request contains the required test code.)

Azure CLI is a large open-source project, we have dozens of modules.
And every day we need to check all the new pull requests and issues, then route them to different service teams or CLI teams.
So I add a Microsoft bot to our repositories.
It can automatically analyze our pull requests and issues.
Now we can:
Auto-assign labels based on an issue or a pull-request description.
Auto-assign assignees or reviewers based on labels.
Auto notify people if they have no response for a long time then we will close it.
Auto verify PR title and history notes in every pull request.
This is a big project, and I'm still optimizing the bot, so I haven't demoed it in the sprint review meeting for now.

Now I am focusing on Test speed enhancement:
I will demo this new improvement at the sprint review meeting on Friday.
In the past, our automation full test will cost more than 70 minutes
first step, 
I add a new argument to record the time spent on each test
And after we Fix the top N slowest tests, it will cost like 50 minutes.
Second step, 
I enable group worker in our test framework, it will spawn a number of workers processes equal to the number of available CPUs, and distribute the tests randomly across them.
After this step, our automation full test will cost like 30 minutes.
Third step,
I split every automation full test into 8 pipeline instances
Using 8 instances is the best practice based on repeated testing ( N = 8 )
Now we need to support 3 python versions: 3.6 3.8 3.10, So we have 24 ( 3 * times 8 ) instances are running in parallel
If you add more instances, some instances will be waiting, and the actual execution time will be longer.
Automatic scheduling modules in every pipeline job
In the past, we test modules order by their name. It will waste a lot of time.
So I write a greedy algorithm to distribute modules to each worker
For each module, we record their historical execution time
Then we assign the module to a worker with the fewest jobs currently
Because we want to ensure the execution time of each worker is the same
For newly added module use module average test time to calculate


Now our team workload is large, so we don't have sufficient time for learning
But we already have a meeting to discuss this.
We need to improve engineering efficiency.
I think my work will save a lot of time for our developers
And we will have codegen version 2 in the future to save our time.( Rukai Ethan and Zhiyi are developing this tool)
And we need deep learning from our daily work
If we have sufficient time, we can do some knowledge sharing.

I need to cook three meals a day and take care of my wife because she is pregnant
Due date is late June 预产期六月下旬
Three people in our building have been infected with the virus
Covid-19 Nucleic Acid PCR Test is required every day
The conditions of working from home are also worse than working in the company
I can only write code on my laptop, I miss my screen monitors in the office.
