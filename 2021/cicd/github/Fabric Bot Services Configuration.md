1. Add needs triage label to new issues
Event responder - issues
Conditions:
 - is action: Opened 
 - not is part of any project
 - not is assigned to somoone
 - not is labeled
Actions:
 - add label: needs-triage
 
2. Replace needs author feedback label with needs attention label when the author comments on an issue
Event responder - issue comments
Conditions:
 - is action: Created
 - is activity sender: Author
 - Has label: needs-author-feedback
 - is open
Actions:
 - Add label: needs-team-attention
 - Remove label: needs-author-feedback

TODO test
3. Remove no recent activity label from issues
Event responder - issues
Conditions:
 - not is action: closed
 - Has label: no-recent-activity
Actions:
 - Remove label: no-recent-activity

TODO test
4. Remove no recent activity label when an issue is commented on
Event responder - issue comments
Conditions:
Has label: no-recent-activity
Actions:
Remove label: no-recent-activity

5. Close stale issues
Scheduled search
Frequency:
 - Every day at 1:00am
Search terms:
 - is issue
 - is open
 - Has label: needs-author-feedback
 - Has label: no-recent-activity
 - No activity since: 14
Action:
 - Close

6. Add no recent activity label to issues
Scheduled search
Frequency:
- Every 6 hours, 4 times a day.
Search terms:
- is issue
- is open
- Has label: needs-author-feedback
- no activity since: 7
- does not have label: no-recent-activity
Actions:
- add label: no-recent-activity
- add reply: xxx

7. Remove needs-triage label on issues once they are labeled
Event responder - issues
Conditions:
- is action: labeled
- has label: needs-triage
- not label added: needs-triage
Actions:
- remove label: needs-triage

8. Add question label to new issues
Event responder - issues
Conditions:
- is action: opened
  - not activity sender has permissions: write
  - not activity sender has permissions: admin
  - not activity sender has association: member
  - not activity sender has association: collaborator
Actions:
  - add label: question

9. For issues closed due to inactivity, re-open an issue if issue author posts a reply within 7 days.
Event responder - issue comments
Actions:
 - not is open
 - is action: created
 - has label: no-recnet-activity
 - has label: needs-author-feedback
 - not no activity since: 7 days
 - not is close and comment action
 - is activity sender: author
 - activity sender has permissions: None TODO
Actions:
 - reopen issue
 - remove label: no-recent-activity
 - remove label: needs-author-feedback
 - add label: needs-team-attention

10. For issues closed with no activity over 7 days, ask non-contributor to consider opening a new issue instead.
Event responder - issue comments
Conditions:
 - is action: Created
 - not is open
 - activity sender has permissions: none
 - no activity since: 7 days
 - not is close and comment action
Actions:
 - add reply: xxx

11. Add label after "Service Attention" is removed
Event responder - issues
Conditions:
 - is open
 - has label: customer-reported
 - label removed: service attention
Actions:
 - add label: needs-team-triage

12. Assign service attention issues to mentionees for MySQL (requested by service team)
Scheduled search
Frequency:
 - Every 3 hours, 8 times a day.
Search terms:
 - is open
 - has label: MySQL
 - has label: Service Attention
 - not assigned to anyone
Actions:
 - Assign to users: MariaDB and MySQL Contacts

13. Assign service attention issues to mentionees for MariaDB (requested by service team)
Scheduled search
Frequency:
 - Every 3 hours, 8 times a day.
Search terms:
 - is open
 - has label: MariaDB
 - has label: Service Attention
 - not assigned to anyone
Actions:
 - Assign to users: MariaDB and MySQL Contacts

14. Triage issues to the service team
Issue Routing - @Mention
Issue routes:
 - labels: Service Attention & AAD; mentionees: adamedx
 ...
Actions:
 - Thanks for the feedback! We are routing this to the appropriate team for follow-up. cc ${mentionees}.

15. Add customer-reported label to PRs from customers
Event responder - pull requests 
Conditions:
 - is action: Opened
   - not activity sender has permissions: Write
   - not activity sender has permissions: Admin
   - not activity sender has association: Member
   - not activity sender has association: Collaborator
Actions:
   - add label: customer-reported
   - add reply: Thank you for your contribution ${issueAuthor}! We will review the pull request and get back to you soon.

16. Add customer-reported label to issues coming from non-collaborators
Event responder - issues
Conditions:
- is action: opened
  - not activity sender has permissions: Write
  - not activity sender has permissions: Admin
  - not activity sender has association: Member
  - not activity sender has association: Collaborator
Actions:
  - add label: customer-reported
  - add label: question

TODO discuss
需要占用很多的task
17. [Network] auto assign labels and users based on issue description. Please do not delete
Event responder - issues
Conditions:
 - is open
 - has label: needs-triage
 - or
   - Title contains az network
   - Issue body contains az network
   - X Title contains [Bb][Oo][Tt] [Tt][Ee][Ss][Tt]
   - X Issue body contains [Bb][Oo][Tt] [Tt][Ee][Ss][Tt]
Actions:
 - Add label: Network
 - X add reply: Network.
 - add milestone: Backlog
 - Assign ot users: Azure CLI Network yonzhan;jsntcy;kairu-ms
 - Remove label: needs-triage

18. [CXP Pilot] CXP Attention Responder
Event responder - issues
Conditions:
 - Is open
 - Label added: CXP Attention
 - not Has label: Service Attention
Actions:
 - Add reply: Thank you for your feedback.  This has been routed to the support team for assistance.

19. [CXP Pilot] CXP Attention Responder
Event responder - issues
Conditions:
 - Is open
 - Label added: CXP Attention
 - Has label: Service Attention
Actions:
 - Add reply: Thank you for your feedback.  This has been routed to the support team for assistance.

TODO discuss test 
应该使用哪一种？
20. Test Auto assign labels based on PR file paths. Please do not delete
模糊匹配, 一个task搞定
Compute: src/azure-cli/azure/cli/command_modules/vm
Network: src/azure-cli/azure/cli/command_modules/network
TODO: 
- 测试 pr 的 label 通知 
- 测试 单label 和 多label的通知

21. Test Auto assign reviewers and assignee based on labels. Please do not delete.
Issue Routing - @Mention
Network xxx
Compute xxx
如果使用了 17 23 24 不需要此步骤

【不支持】 Auto assign milestone based on PR creation date.
直接加到一个固定的milestone,一个月维护一次。 
- 需要把加milestone的单独抽出一个任务
- 所有的issue都加嘛

22. [Compute] auto assign labels and users based on issue description. Please do not delete
Event responder - issues
Conditions:
 - is open
 - has label: needs-triage
 - or
   - Title contains az vm
   - Issue body contains az vm
   - X Title contains [Bb][Oo][Tt] [Tt][Ee][Ss][Tt]
   - X Issue body contains [Bb][Oo][Tt] [Tt][Ee][Ss][Tt]
Actions:
 - Add label: Compute
 - X add reply: Compute.
 - add milestone: Backlog
 - Assign ot users: Azure CLI Compute yonzhan;zhoxing-ms
 - Remove label: needs-triage

23. [Storage] auto assign labels and users based on issue description. Please do not delete
Event responder - issues
Conditions:
 - is open
 - has label: needs-triage
 - or
   - Title contains az storage
   - Issue body contains az storage
   - X Title contains [Bb][Oo][Tt] [Tt][Ee][Ss][Tt]
   - X Issue body contains [Bb][Oo][Tt] [Tt][Ee][Ss][Tt]
Actions:
 - Add label: Storage
 - X add reply: Storage.
 - add milestone: Backlog
 - Assign ot users: Azure CLI Storage yonzhan;
 - Remove label: needs-triage

24. [Network] Auto assign labels and reviewers based on PR title/description. Please do not delete
Event responder - pull requests
Conditions:
 - is open
 - or
   - Title contains az network
   - Issue body contains az network
Actions:
 - X add reply: Network.
 - X add milestone: Backlog
 - Add label: Network
 - Request reviewer: yonzhan
 - Request reviewer: jsntcy
 - Request reviewer: kairu-ms
 
25. [Compute] Auto assign labels and reviewers based on PR title/description. Please do not delete
Event responder - pull requests
Conditions:
 - is open
 - or
   - Title contains az vm
   - Issue body contains az vm
Actions:
 - Add label: Compute
 - X add reply: Compute.
 - X add milestone: Backlog
 - Request reviewer: yonzhan
 - Request reviewer: zhoxing-ms

26. [Storage] Auto assign labels and reviewers based on PR title/description. Please do not delete
Event responder - pull requests
Conditions:
 - is open
 - or
   - Title contains az storage
   - Issue body contains az storage
Actions:
 - Add label: Storage
 - X add reply: Storage.
 - X add milestone: Backlog
 - Request reviewer: yonzhan
 - Request reviewer: evelyn-ys
 
[Network] Auto assign reviewers and assignee based on labels. Please do not delete. 不需要了
Event responder - pull requests
Conditions:
 - is open
 - Has label: Network
Actions:
 - Request reviewer: yonzhan
 - Request reviewer: jsntcy
 - Request reviewer: kairu-ms
问题： TODO
 - 如何做到reviewer不包含创建人自己？

【不支持】【待确认】 TODO
Notify PR creators when the PR created cannot be released in this sprint (created in the last week of the sprint)

【不支持】【待确认】 TODO
discuss Notify PR creator when CI fail.

【不支持】【待确认】 27. Verify PR title, history notes to make it more standard to reduce manual effort during release.
Event responder - pull requests
[Monitor] `az monitor log-analytics workspace table`: Add new command `create` and `delete` to support table operations,
          `az monitor log-analytics workspace update`: Add a new parameter `--data-collection-rule` to support update defaultDataCollectionRuleResourceId
- 以 `[` 开头的才判断
- ] 之后需要有空格
- `az `之前的内容需要匹配 \` 符号
- `:` 之后需要有一个空格
- `: ` 之后的第一个字符大写
- commnad, parameter, argument 后面的字符需要 \`
- `--` 开头的单词 需要有 \`  
[Component Name 1] BREAKING CHANGE: `az command a`: Make some customer-facing breaking change.  
[Component Name 2] `az command b`: Add some customer-facing feature.  
[App Service] `az staticwebapp create` : Change default output location to None. Remove unnecessary properties from output  
[App Service] `az staticwebapp show` : Remove unnecessary properties from output  
[App Service] `az staticwebapp list` : Remove unnecessary properties from output  
[App Service] `az staticwebapp update` : Remove unnecessary properties from output  
- 以 `[` 开头的 且不是形如 [Component Name 的 才判断
- ] 之后需要有空格
- `az `之前的内容需要匹配 \` 符号
- `:` 之后需要有一个空格
- `: ` 之后的第一个字符大写 
- commnad, parameter, argument 后面的字符需要 \`
- `--` 开头的单词 需要有 \`  
Conditions:
- Title contains
- Pull request body contains
- is open
- Has label: Test (To delete)
Actions:
- Request changes on a pull requst

【不支持】【待确认】 28. Scheduled search 
Frequency
- every hour
Search terms
- Is open
- Is pull request
- Does not have label: Pass-verify-PR
- Have label: test
Actions:
- Add label: Need-verify-PR

【不支持】【待确认】 TODO
discuss Show date for code freeze and release in PR page (template or GitHub banner).

Merge PR only have json file - azure-cli-extensions 
Auto-merge pull requests

---

Nice to have:
TODO Friendly bot

TODO Soft-Close stale issues over a 150 days

TODO Close issues with nothing in the body

---

time:
 - No activity since x days
 - Created after/before x days

