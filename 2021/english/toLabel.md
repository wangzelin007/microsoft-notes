Hope you’re safe and doing good.  
I am following up on this case as I haven’t heard back from you in a while and I am concerned about your case being idle.  
Please let me know, if you need any support from Microsoft. Or if the issue is resolved, please confirm if I can close the case.  
May I ask could you add scenario tests and examples for these new commands?
Our release day is the end of each month, so I will move it to the next milestone on the 20th of each month before this feature is GA.

hotfix：
We have fixed schedule once a month as you can see https://github.com/Azure/azure-cli/milestones
We don't release bugfix version often only if you have strong proof that you really need this.
Like some investigation data about how many customers influenced/how many users ask for this since they are blocked.

CI error:
Could you pull the latest code from remote main branch first, and then fix the CI style check issue below.
After that, we will help you solve the remainning CI issue later.
git rebase dev
