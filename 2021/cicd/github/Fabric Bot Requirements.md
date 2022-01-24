- Issues:
  - (done) Auto assign labels based on issue description.
  - (done) Auto assign assignees based on labels.
    - Label-assignee mapping for service team (service attention): https://dev.azure.com/azure-sdk/internal/_wiki/wikis/internal.wiki/43/Service-Team-Label-and-Contact-List
    - Label-assignee mapping for CLI team: Prerequisites: Add two columns (label and owners) in https://github.com/Azure/azure-cli/blob/dev/doc/modules_owned_by_cli_team.md
  - 【待确认】 TODO Auto assign milestone based on issue creation date. 
  - 【不支持】 SLA don’t count bot comments | Auto add a comment based on template to avoid issue response SLA. 
  - (done) Auto notify issue creators/resolvers if they have no response for a long time (7 days).
  - (done) Auto close issue if the issue creators have no response longer than 14 days.
    - use label: needs-author-feedback+
- Pull requests:
  - **Auto assign labels based on PR title/description.**
  - **Auto assign reviewers and assignee based on labels.**
  - 【待确认】TODO **Auto assign milestone based on PR creation date.**
  - 【待确认】TODO **Notify PR creators when the PR created cannot be released in this sprint (created in the last week of the sprint)**
  - 【待确认】TODO **Notify PR creator when CI fail.**
  - 【待确认】TODO **Verify PR title, history notes to make it more standard to reduce manual effort during release.**
  - 【待确认】TODO Show date for code freeze and release in PR page (template or GitHub banner). (reply?)

------------------------------------------------------------------------
1. Auto add a comment based on template to avoid issue response SLA.
   - I think we will give up since SLA don’t count bot comments
2. These changes are also very different than what we currently have in the other repositories.
   - But I think OSPO Fabricbot already support these features, we only need to test and configure them.
   - And it will save a lot of time for CLI Team and Service Team.
3. With the move of CLI and powershell outside from DevDiv a separate (but related) question came up – should we now separate the 2 repositories from our reporting and monitoring?
   - I don't think we will move outside from DevDiv, because the only different between Fabric Bot and MSFT Bot is that the former is an internal name and the latter is the public facing name.
   - So we are looking for some advanced configuration to enhance the bot and save time.
-----------------------------------------------------------------------
**We already move from DevDiv to Azure Core**