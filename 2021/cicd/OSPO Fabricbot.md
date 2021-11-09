- Issues:
  - Auto assign labels based on issue description.
  - Auto assign assignees based on labels.
  - Auto assign milestone based on issue creation date.
  - Auto add a comment based on template to avoid issue response SLA.
    - (X) SLA don’t count bot comments
  - Auto notify issue creators/resolvers if they have no response for a long time (7 days).
  - Auto close issue if the issue creators have no response longer than 14 days.
- Pull requests:
  - Auto assign labels based on PR title/description.
  - Auto assign reviewers and assignee based on labels.
  - Auto assign milestone based on PR creation date.
  - Notify PR creators when the PR created cannot be released in this sprint (created in the last week of the sprint)
  - Notify PR creator when CI fail.
  - Verify PR title, history notes to make it more standard to reduce manual effort during release.
  - Show date for code freeze and release in PR page (template or GitHub banner).

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