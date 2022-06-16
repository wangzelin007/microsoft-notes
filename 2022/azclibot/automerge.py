import json
import os
import requests
import sys


url = 'https://api.github.com/repos/wangzelin007/github-bot-tutorial/pulls'

token = os.getenv('GH_AUTH')

headers = {'Authorization': 'token %s' % token}

# -d "{\"title\": \"${pr_title}\", \"body\": \"${pr_body}\", \"head\": \"${pr_head}\", \"base\": \"main\"}"

# pr_title="Update CLI extensions available doc"
# pr_body="${commit_msg}"
# pr_head="azclibot:${temp_branch}"

# commit_msg="${commit_msg_title}\n ${commit_msg_body}\n${extension_commit_url}"
# temp_branch="az-ext-list-ci-$(Build.BuildId)"

# commit_msg_title="Update CLI extensions available doc."
# commit_msg_body="Triggered by Azure CLI Extensions Sync Pipeline - ADO_BUILD_URI=$(Build.BuildId)"
# extension_commit_url="https://github.com/Azure/azure-cli-extensions/commit/${extension_commit_id}"
# extension_commit_id="$(Build.SourceVersion)"

pr_title="Update CLI extensions available doc"
pr_body="Update CLI extensions available doc"
pr_head="wangzelin007:pr_head"


def create_pr():
    body = {
        'title': pr_title,
        'body': pr_body,
        'head': pr_head,
        'base': 'master'
    }

    # r = requests.get(url, headers=headers)
    # "documentation_url":"https://docs.github.com/rest/reference/pulls#create-a-pull-request"
    try:
        r = requests.post(url, json=body, headers=headers)
    except requests.RequestException as e:
        print(e)
    # <Response [201]>
    # text
    # {
    #   "url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/pulls/3",
    #   "id": 948857634,
    #   "node_id": "PR_kwDOG4tT9c44jmsi",
    #   "html_url": "https://github.com/wangzelin007/github-bot-tutorial/pull/3",
    #   "diff_url": "https://github.com/wangzelin007/github-bot-tutorial/pull/3.diff",
    #   "patch_url": "https://github.com/wangzelin007/github-bot-tutorial/pull/3.patch",
    #   "issue_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/issues/3",
    #   "number": 3,
    #   "state": "open",
    #   "locked": false,
    #   "title": "Update CLI extensions available doc",
    #   "user": {
    #     "login": "wangzelin007",
    #     "id": 18628534,
    #     "node_id": "MDQ6VXNlcjE4NjI4NTM0",
    #     "avatar_url": "https://avatars.githubusercontent.com/u/18628534?v\u003d4",
    #     "gravatar_id": "",
    #     "url": "https://api.github.com/users/wangzelin007",
    #     "html_url": "https://github.com/wangzelin007",
    #     "followers_url": "https://api.github.com/users/wangzelin007/followers",
    #     "following_url": "https://api.github.com/users/wangzelin007/following{/other_user}",
    #     "gists_url": "https://api.github.com/users/wangzelin007/gists{/gist_id}",
    #     "starred_url": "https://api.github.com/users/wangzelin007/starred{/owner}{/repo}",
    #     "subscriptions_url": "https://api.github.com/users/wangzelin007/subscriptions",
    #     "organizations_url": "https://api.github.com/users/wangzelin007/orgs",
    #     "repos_url": "https://api.github.com/users/wangzelin007/repos",
    #     "events_url": "https://api.github.com/users/wangzelin007/events{/privacy}",
    #     "received_events_url": "https://api.github.com/users/wangzelin007/received_events",
    #     "type": "User",
    #     "site_admin": false
    #   },
    #   "body": "Update CLI extensions available doc",
    #   "created_at": "2022-05-27T01:39:27Z",
    #   "updated_at": "2022-05-27T01:39:27Z",
    #   "assignees": [],
    #   "requested_reviewers": [],
    #   "requested_teams": [],
    #   "labels": [],
    #   "draft": false,
    #   "commits_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/pulls/3/commits",
    #   "review_comments_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/pulls/3/comments",
    #   "review_comment_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/pulls/comments{/number}",
    #   "comments_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/issues/3/comments",
    #   "statuses_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/statuses/9871570a82592d5c382a810c7cffa2031865fb2b",
    #   "head": {
    #     "label": "wangzelin007:pr_head",
    #     "ref": "pr_head",
    #     "sha": "9871570a82592d5c382a810c7cffa2031865fb2b",
    #     "user": {
    #       "login": "wangzelin007",
    #       "id": 18628534,
    #       "node_id": "MDQ6VXNlcjE4NjI4NTM0",
    #       "avatar_url": "https://avatars.githubusercontent.com/u/18628534?v\u003d4",
    #       "gravatar_id": "",
    #       "url": "https://api.github.com/users/wangzelin007",
    #       "html_url": "https://github.com/wangzelin007",
    #       "followers_url": "https://api.github.com/users/wangzelin007/followers",
    #       "following_url": "https://api.github.com/users/wangzelin007/following{/other_user}",
    #       "gists_url": "https://api.github.com/users/wangzelin007/gists{/gist_id}",
    #       "starred_url": "https://api.github.com/users/wangzelin007/starred{/owner}{/repo}",
    #       "subscriptions_url": "https://api.github.com/users/wangzelin007/subscriptions",
    #       "organizations_url": "https://api.github.com/users/wangzelin007/orgs",
    #       "repos_url": "https://api.github.com/users/wangzelin007/repos",
    #       "events_url": "https://api.github.com/users/wangzelin007/events{/privacy}",
    #       "received_events_url": "https://api.github.com/users/wangzelin007/received_events",
    #       "type": "User",
    #       "site_admin": false
    #     },
    #     "repo": {
    #       "id": 462115829,
    #       "node_id": "R_kgDOG4tT9Q",
    #       "name": "github-bot-tutorial",
    #       "full_name": "wangzelin007/github-bot-tutorial",
    #       "private": false,
    #       "owner": {
    #         "login": "wangzelin007",
    #         "id": 18628534,
    #         "node_id": "MDQ6VXNlcjE4NjI4NTM0",
    #         "avatar_url": "https://avatars.githubusercontent.com/u/18628534?v\u003d4",
    #         "gravatar_id": "",
    #         "url": "https://api.github.com/users/wangzelin007",
    #         "html_url": "https://github.com/wangzelin007",
    #         "followers_url": "https://api.github.com/users/wangzelin007/followers",
    #         "following_url": "https://api.github.com/users/wangzelin007/following{/other_user}",
    #         "gists_url": "https://api.github.com/users/wangzelin007/gists{/gist_id}",
    #         "starred_url": "https://api.github.com/users/wangzelin007/starred{/owner}{/repo}",
    #         "subscriptions_url": "https://api.github.com/users/wangzelin007/subscriptions",
    #         "organizations_url": "https://api.github.com/users/wangzelin007/orgs",
    #         "repos_url": "https://api.github.com/users/wangzelin007/repos",
    #         "events_url": "https://api.github.com/users/wangzelin007/events{/privacy}",
    #         "received_events_url": "https://api.github.com/users/wangzelin007/received_events",
    #         "type": "User",
    #         "site_admin": false
    #       },
    #       "html_url": "https://github.com/wangzelin007/github-bot-tutorial",
    #       "description": "learn github bot",
    #       "fork": false,
    #       "url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial",
    #       "forks_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/forks",
    #       "keys_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/keys{/key_id}",
    #       "collaborators_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/collaborators{/collaborator}",
    #       "teams_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/teams",
    #       "hooks_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/hooks",
    #       "issue_events_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/issues/events{/number}",
    #       "events_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/events",
    #       "assignees_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/assignees{/user}",
    #       "branches_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/branches{/branch}",
    #       "tags_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/tags",
    #       "blobs_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/git/blobs{/sha}",
    #       "git_tags_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/git/tags{/sha}",
    #       "git_refs_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/git/refs{/sha}",
    #       "trees_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/git/trees{/sha}",
    #       "statuses_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/statuses/{sha}",
    #       "languages_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/languages",
    #       "stargazers_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/stargazers",
    #       "contributors_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/contributors",
    #       "subscribers_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/subscribers",
    #       "subscription_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/subscription",
    #       "commits_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/commits{/sha}",
    #       "git_commits_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/git/commits{/sha}",
    #       "comments_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/comments{/number}",
    #       "issue_comment_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/issues/comments{/number}",
    #       "contents_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/contents/{+path}",
    #       "compare_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/compare/{base}...{head}",
    #       "merges_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/merges",
    #       "archive_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/{archive_format}{/ref}",
    #       "downloads_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/downloads",
    #       "issues_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/issues{/number}",
    #       "pulls_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/pulls{/number}",
    #       "milestones_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/milestones{/number}",
    #       "notifications_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/notifications{?since,all,participating}",
    #       "labels_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/labels{/name}",
    #       "releases_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/releases{/id}",
    #       "deployments_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/deployments",
    #       "created_at": "2022-02-22T03:01:19Z",
    #       "updated_at": "2022-02-22T03:01:36Z",
    #       "pushed_at": "2022-05-27T01:31:44Z",
    #       "git_url": "git://github.com/wangzelin007/github-bot-tutorial.git",
    #       "ssh_url": "git@github.com:wangzelin007/github-bot-tutorial.git",
    #       "clone_url": "https://github.com/wangzelin007/github-bot-tutorial.git",
    #       "svn_url": "https://github.com/wangzelin007/github-bot-tutorial",
    #       "size": 7,
    #       "stargazers_count": 0,
    #       "watchers_count": 0,
    #       "language": "Python",
    #       "has_issues": true,
    #       "has_projects": true,
    #       "has_downloads": true,
    #       "has_wiki": true,
    #       "has_pages": false,
    #       "forks_count": 1,
    #       "archived": false,
    #       "disabled": false,
    #       "open_issues_count": 3,
    #       "allow_forking": true,
    #       "is_template": false,
    #       "topics": [],
    #       "visibility": "public",
    #       "forks": 1,
    #       "open_issues": 3,
    #       "watchers": 0,
    #       "default_branch": "master"
    #     }
    #   },
    #   "base": {
    #     "label": "wangzelin007:master",
    #     "ref": "master",
    #     "sha": "59037ec24171f6b086eaac63ce03d2d07252d955",
    #     "user": {
    #       "login": "wangzelin007",
    #       "id": 18628534,
    #       "node_id": "MDQ6VXNlcjE4NjI4NTM0",
    #       "avatar_url": "https://avatars.githubusercontent.com/u/18628534?v\u003d4",
    #       "gravatar_id": "",
    #       "url": "https://api.github.com/users/wangzelin007",
    #       "html_url": "https://github.com/wangzelin007",
    #       "followers_url": "https://api.github.com/users/wangzelin007/followers",
    #       "following_url": "https://api.github.com/users/wangzelin007/following{/other_user}",
    #       "gists_url": "https://api.github.com/users/wangzelin007/gists{/gist_id}",
    #       "starred_url": "https://api.github.com/users/wangzelin007/starred{/owner}{/repo}",
    #       "subscriptions_url": "https://api.github.com/users/wangzelin007/subscriptions",
    #       "organizations_url": "https://api.github.com/users/wangzelin007/orgs",
    #       "repos_url": "https://api.github.com/users/wangzelin007/repos",
    #       "events_url": "https://api.github.com/users/wangzelin007/events{/privacy}",
    #       "received_events_url": "https://api.github.com/users/wangzelin007/received_events",
    #       "type": "User",
    #       "site_admin": false
    #     },
    #     "repo": {
    #       "id": 462115829,
    #       "node_id": "R_kgDOG4tT9Q",
    #       "name": "github-bot-tutorial",
    #       "full_name": "wangzelin007/github-bot-tutorial",
    #       "private": false,
    #       "owner": {
    #         "login": "wangzelin007",
    #         "id": 18628534,
    #         "node_id": "MDQ6VXNlcjE4NjI4NTM0",
    #         "avatar_url": "https://avatars.githubusercontent.com/u/18628534?v\u003d4",
    #         "gravatar_id": "",
    #         "url": "https://api.github.com/users/wangzelin007",
    #         "html_url": "https://github.com/wangzelin007",
    #         "followers_url": "https://api.github.com/users/wangzelin007/followers",
    #         "following_url": "https://api.github.com/users/wangzelin007/following{/other_user}",
    #         "gists_url": "https://api.github.com/users/wangzelin007/gists{/gist_id}",
    #         "starred_url": "https://api.github.com/users/wangzelin007/starred{/owner}{/repo}",
    #         "subscriptions_url": "https://api.github.com/users/wangzelin007/subscriptions",
    #         "organizations_url": "https://api.github.com/users/wangzelin007/orgs",
    #         "repos_url": "https://api.github.com/users/wangzelin007/repos",
    #         "events_url": "https://api.github.com/users/wangzelin007/events{/privacy}",
    #         "received_events_url": "https://api.github.com/users/wangzelin007/received_events",
    #         "type": "User",
    #         "site_admin": false
    #       },
    #       "html_url": "https://github.com/wangzelin007/github-bot-tutorial",
    #       "description": "learn github bot",
    #       "fork": false,
    #       "url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial",
    #       "forks_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/forks",
    #       "keys_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/keys{/key_id}",
    #       "collaborators_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/collaborators{/collaborator}",
    #       "teams_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/teams",
    #       "hooks_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/hooks",
    #       "issue_events_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/issues/events{/number}",
    #       "events_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/events",
    #       "assignees_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/assignees{/user}",
    #       "branches_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/branches{/branch}",
    #       "tags_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/tags",
    #       "blobs_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/git/blobs{/sha}",
    #       "git_tags_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/git/tags{/sha}",
    #       "git_refs_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/git/refs{/sha}",
    #       "trees_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/git/trees{/sha}",
    #       "statuses_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/statuses/{sha}",
    #       "languages_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/languages",
    #       "stargazers_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/stargazers",
    #       "contributors_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/contributors",
    #       "subscribers_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/subscribers",
    #       "subscription_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/subscription",
    #       "commits_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/commits{/sha}",
    #       "git_commits_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/git/commits{/sha}",
    #       "comments_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/comments{/number}",
    #       "issue_comment_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/issues/comments{/number}",
    #       "contents_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/contents/{+path}",
    #       "compare_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/compare/{base}...{head}",
    #       "merges_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/merges",
    #       "archive_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/{archive_format}{/ref}",
    #       "downloads_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/downloads",
    #       "issues_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/issues{/number}",
    #       "pulls_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/pulls{/number}",
    #       "milestones_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/milestones{/number}",
    #       "notifications_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/notifications{?since,all,participating}",
    #       "labels_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/labels{/name}",
    #       "releases_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/releases{/id}",
    #       "deployments_url": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/deployments",
    #       "created_at": "2022-02-22T03:01:19Z",
    #       "updated_at": "2022-02-22T03:01:36Z",
    #       "pushed_at": "2022-05-27T01:31:44Z",
    #       "git_url": "git://github.com/wangzelin007/github-bot-tutorial.git",
    #       "ssh_url": "git@github.com:wangzelin007/github-bot-tutorial.git",
    #       "clone_url": "https://github.com/wangzelin007/github-bot-tutorial.git",
    #       "svn_url": "https://github.com/wangzelin007/github-bot-tutorial",
    #       "size": 7,
    #       "stargazers_count": 0,
    #       "watchers_count": 0,
    #       "language": "Python",
    #       "has_issues": true,
    #       "has_projects": true,
    #       "has_downloads": true,
    #       "has_wiki": true,
    #       "has_pages": false,
    #       "forks_count": 1,
    #       "archived": false,
    #       "disabled": false,
    #       "open_issues_count": 3,
    #       "allow_forking": true,
    #       "is_template": false,
    #       "topics": [],
    #       "visibility": "public",
    #       "forks": 1,
    #       "open_issues": 3,
    #       "watchers": 0,
    #       "default_branch": "master"
    #     }
    #   },
    #   "_links": {
    #     "self": {
    #       "href": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/pulls/3"
    #     },
    #     "html": {
    #       "href": "https://github.com/wangzelin007/github-bot-tutorial/pull/3"
    #     },
    #     "issue": {
    #       "href": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/issues/3"
    #     },
    #     "comments": {
    #       "href": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/issues/3/comments"
    #     },
    #     "review_comments": {
    #       "href": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/pulls/3/comments"
    #     },
    #     "review_comment": {
    #       "href": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/pulls/comments{/number}"
    #     },
    #     "commits": {
    #       "href": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/pulls/3/commits"
    #     },
    #     "statuses": {
    #       "href": "https://api.github.com/repos/wangzelin007/github-bot-tutorial/statuses/9871570a82592d5c382a810c7cffa2031865fb2b"
    #     }
    #   },
    #   "author_association": "OWNER",
    #   "merged": false,
    #   "mergeable_state": "unknown",
    #   "comments": 0,
    #   "review_comments": 0,
    #   "maintainer_can_modify": false,
    #   "commits": 1,
    #   "additions": 1,
    #   "deletions": 0,
    #   "changed_files": 1
    # }
    if r.status_code != 201:
        print(r)
        print(r.text)
        sys.exit(1)

    number = json.loads(r.text)['number']
    return number

def auto_merge(number):
    # https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/merge
    # curl -X PUT https://api.github.com/repos/wangzelin007/github-bot-tutorial/pulls/3/merge
    merge_url = f'https://api.github.com/repos/wangzelin007/github-bot-tutorial/pulls/{number}/merge'
    # merge, squash or rebase
    body = {
        'merge_method': 'rebase'
    }
    try:
        r = requests.put(merge_url, json=body, headers=headers)
    except requests.RequestException as e:
        print(e)
    if r.status_code != 200:
        print(r)
        print(r.text)
        sys.exit(1)

"""
set -ev

echo $(pwd)

# git config
GITHUB_TOKEN=$(az keyvault secret show --vault-name kv-azuresdk --name azclibot-pat --query value -otsv)

git config --global user.email "AzPyCLI@microsoft.com"
git config --global user.name "Azure CLI Team"

git remote add azclibot https://azclibot:${GITHUB_TOKEN}@github.com/azclibot/azure-cli-extensions.git

git status

#touch upgrade_extensions.txt
#echo "virtual-wan" >> upgrade_extensions.txt 
#echo "storage-preview" >> upgrade_extensions.txt

if [[ ! -f "upgrade_extensions.txt" ]]; then
    echo "no extension upgrade, no need to create PR (1)."
    exit 0
fi

if [[ -z "$(git status --short src/index.json)" ]]; then
    echo "no extension upgrade, no need to create PR (2)."
    exit 0
fi

#######################
# prepare 
#######################

upgraded_extensions=""
for extension in $(cat upgrade_extensions.txt)
do
    ext=`echo $extension | sed -e 's/\n//'`
    upgraded_extensions+="[ $ext ] "
done

extension_commit_id="$(Build.SourceVersion)"

commit_url="https://github.com/Azure/azure-cli-extensions/commit/${extension_commit_id}"
commit_msg_title="[Release] Update index.json for extension $upgraded_extensions"
commit_msg_body="Triggered by Azure CLI Extensions Release Pipeline - ADO_BUILD_ID=$(Build.BuildId)"
commit_msg="${commit_msg_title}\n\n ${commit_msg_body}\n\nLast commit against main: ${commit_url}"


#######################
# save branch
#######################

temp_branch="release-$(date +%Y%m%d-%H%M%S)"
git checkout -b "$temp_branch"
git add src/index.json
git commit -m "${commit_msg_title}" -m "${commit_msg_body}" -m "Last commit: ${commit_url}"
git push -u azclibot "$temp_branch"


#######################
# ceate PR
#######################

pr_title="$commit_msg_title"
pr_body="$commit_msg"
pr_head="azclibot:${temp_branch}"

curl \
-H "Authorization: token ${GITHUB_TOKEN}" \
-d "{\"title\": \"${pr_title}\", \"body\": \"${pr_body}\", \"head\": \"${pr_head}\", \"base\": \"main\"}" \
https://api.github.com/repos/Azure/azure-cli-extensions/pulls
"""

# resp = $(curl -H "Authorization: token ${GITHUB_TOKEN}" -d "{\"title\": \"${pr_title}\", \"body\": \"${pr_body}\", \"head\": \"${pr_head}\", \"base\": \"main\"}" https://api.github.com/repos/Azure/azure-cli-extensions/pulls)
# number = json.loads(resp)['number']
def create_pr2():
    import subprocess
    body = {
        "title": pr_title,
        "body": pr_body,
        "head": pr_head,
        "base": "master"
    }
    body = json.dumps(body)

    # r = requests.get(url, headers=headers)
    # "documentation_url":"https://docs.github.com/rest/reference/pulls#create-a-pull-request"
    cURL = r"""curl -H "Authorization: token ${GITHUB_TOKEN}" -d "{\"title\": \"${pr_title}\", \"body\": \"${pr_body}\", \"head\": \"${pr_head}\", \"base\": \"main\"}" https://api.github.com/repos/Azure/azure-cli-extensions/pulls
    """
    import shlex
    lCmd = shlex.split(cURL)
    print(lCmd)
    cmd = ['curl', '-H', f'Authorization: token {token}', '-d',
           f'{body}',
           f'{url}']
    print(cmd)
    try:
        resp = subprocess.run(cmd, check=True, stdout=subprocess.PIPE)
    except subprocess.CalledProcessError:
        error_flag = True
    number = json.loads(resp.stdout.decode("UTF-8"))['number']
    return number

def auto_merge2(number):
    # https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/merge
    # curl -X PUT https://api.github.com/repos/wangzelin007/github-bot-tutorial/pulls/3/merge
    merge_url = f'https://api.github.com/repos/wangzelin007/github-bot-tutorial/pulls/{number}/merge'
    # merge, squash or rebase
    body = {
        'merge_method': 'rebase'
    }
    try:
        r = requests.put(merge_url, json=body, headers=headers)
    except requests.RequestException as e:
        print(e)
    if r.status_code != 200:
        print(r)
        print(r.text)
        sys.exit(1)

if __name__ == '__main__':
    # number = create_pr()
    # number = 6
    # auto_merge(number)
    resp = create_pr2()
    auto_merge2(resp)