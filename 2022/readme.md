1. Test/CI Enhancements
   -- extension live test
   -- Faster test run
     -- pipeline optimization
     -- pytest optimization
     -- Distributed optimization
   -- test relationship. (bump sdk)
   -- extension command test coverage
2. azure cli bot 
   -- auto reply to avoid issue response SLA.
   -- pipeline result displayed on GitHub
   -- time related
      -- Auto assign milestone based on issue/PR creation date. 
      -- Auto notify issue creators/resolvers if they have no response for a long time (7 days).
      -- Auto close issue if the issue creators have no response longer than 14 days.
      -- Notify PR creators when the PR created cannot be released in this sprint (created in the last week of the sprint)
      -- Notify PR creator when CI fail.
      -- Show date for code freeze and release in PR page (template or GitHub banner).
   -- auto merge pr
   -- auto re-run check pr task when user modify PR title or content
   -- auto generate fabric.json
3. Bump sdk pipeline support
-- test readme in [PR](https://github.com/Azure/azure-cli-extensions/pull/4499)