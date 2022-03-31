git version
git lfs version
git init "/home/vsts/work/1/s"
```
git remote: Manage set of tracked repositories
Add a remote named <name> for the repository at <URL>. The command git fetch <name> can then be used to create and update remote-tracking branches <name>/<branch>.
git remote add [-t <branch>] [-m <master>] [-f] [--[no-]tags] [--mirror=(fetch|push)] <name> <URL>
```
git remote add origin https://github.com/Azure/azure-cli
git config gc.auto 0
git config --get-all http.https://github.com/Azure/azure-cli.extraheader
git config --get-all http.extraheader
git config --get-regexp .*extraheader
git config --get-all http.proxy
git config http.version HTTP/1.1
```
fetch from the origin first
--depth=1 获取最后一次？
```
git fetch --force --tags --prune --prune-tags --progress --no-recurse-submodules origin --depth=1 +2675aeab8b20ab818765b5518d99c4200d94528e:refs/remotes/origin/2675aeab8b20ab818765b5518d99c4200d94528e
```
git-fetch - Download objects and refs from another repository
git fetch [<options>] [<repository> [<refspec>…]]
<refspec> Specifies which refs to fetch and which local refs to update.
<refspec> 参数的格式是可选的加号 +，后跟源 <src>，后跟冒号 :，后跟目标 ref <dst>。 <dst> 为空时，可以省略冒号。

远程引用，类似于 .git/refs/heads 中存储的本地仓库各分支的最后一次提交，在 .git/refs/remotes 是用来记录多个远程仓库各分支的最后一次提交。
```
git fetch --force --tags --prune --prune-tags --progress --no-recurse-submodules origin --depth=1 +2675aeab8b20ab818765b5518d99c4200d94528e
```
checkout 到合并后的分支
```
git checkout --progress --force refs/remotes/origin/2675aeab8b20ab818765b5518d99c4200d94528e

git log --graph --pretty=oneline
* 2675aeab8b20ab818765b5518d99c4200d94528e (grafted, HEAD, origin/2675aeab8b20ab818765b5518d99c4200d94528e) Merge 1cfe15b72a4aaebf7971cdf8e3bffdeb28cb7fdf into b401e2c4ecda4966957bc2b3179d45a2aaaea6f6

$ git fetch origin 2675aeab8b20ab818765b5518d99c4200d94528e
$ git checkout 2675aeab8b20ab818765b5518d99c4200d94528e
$ git log --graph --pretty=oneline

PR automated for：
https://dev.azure.com/azure-sdk/public/_build?definitionId=246&_a=summary
可以看出来都是一个merge commit

Batch CI for：
是一个全量的automation full test(merge 之后自动触发)
自己的分支也会触发是因为，自己的branch提交后默认就是merge了。

https://github.com/Azure/azure-cli-extensions/issues/4565
