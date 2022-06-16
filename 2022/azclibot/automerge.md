curl -H "Authorization: token ${GITHUB_TOKEN}" https://api.github.com/repos/Azure/azure-cli-extensions/pulls | grep "${pr_title}" | cat

curl \
-H "Authorization: token ${GITHUB_TOKEN}" \
-d "{\"title\": \"${pr_title}\", \"body\": \"${pr_body}\", \"head\": \"${pr_head}\", \"base\": \"main\"}" \
https://api.github.com/repos/Azure/azure-cli-extensions/pulls

curl \
-H "Authorization: token ${GITHUB_TOKEN_EXTENSIONS_SYNC_TO_MICROSOFT_DOCS}" \
-d "{\"title\": \"${pr_title}\", \"body\": \"${pr_body}\", \"head\": \"${pr_head}\", \"base\": \"main\"}" \
https://api.github.com/repos/MicrosoftDocs/azure-docs-cli/pulls

Build_BuildNumber
example:
https://dev.azure.com/azure-sdk/internal/_releaseDefinition?definitionId=94&_a=definition-tasks&environmentId=195

1. 直接 push commit
temp_branch="release-$(date +%Y%m%d-%H%M%S)"
git checkout -b "$temp_branch"
git add src/index.json
git commit -m "${commit_msg_title}" -m "${commit_msg_body}" -m "Last commit: ${commit_url}"
git push -u azclibot "$temp_branch"
2. create a comment in pr
https://docs.github.com/en/rest/pulls/comments#create-a-review-comment-for-a-pull-request
3. Build_BuildNumber
