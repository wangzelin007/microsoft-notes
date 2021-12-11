# Repo('.', odbt=git.db.GitDB)
# git diff 5bca3e126 8f28e9818 --stat
# source_commit = git_repo.commit('20141')
# target_commit = git_repo.commit('upstream/dev')
# source_commit = git_repo.commit('5bca3e126')
# target_commit = git_repo.commit('8f28e9818')
#
# diffs = target_commit.diff(source_commit)
# diff = diffs[0]
# diff.a_blob.data_stream.read()
# diff.b_blob.data_stream
# diff.b_blob.data_stream.read()
#
# os.system('git diff 5bca3e126 8f28e9818')

diffs[-1].a_blob.data_stream.read()
diffs[-1].b_blob.data_stream.read()

from subprocess import run
# 这是一个调用winscp传输文件到Linux的命令，使用os.system()执行会弹出一个命令框
command2 = 'git diff 5bca3e126 8f28e9818'
run(command2,shell=True)
run("cd /d/code/azure-cli", shell=True)
# cd D:\code\azure-cli && git diff 5bca3e126 8f28e9818cd
run('git diff 5bca3e126 8f28e9818', shell=True)

# [difflib](https://docs.python.org/zh-cn/3/library/difflib.html)
import difflib
difflib.context_diff(diff.a_blob.data_stream.read(), diff.b_blob.data_stream.read())

# ---ok---
print(''.join(
    context_diff(diff_index[-1].a_blob.data_stream.read().decode("utf-8") .splitlines(True),
                 diff_index[-1].b_blob.data_stream.read().decode("utf-8") .splitlines(True),
                 'Original', 'Current')),
    end="")

from difflib import context_diff
from pprint import pprint

for diff in diff_index:
    filename = diff.a_path.split('/')[-1].split('.')[0]
    if 'params' in filename or 'commands' in filename or filename.startswith('test_'):
        # _params, commands, test_*
        # print(''.join(
        #     context_diff(diff.a_blob.data_stream.read().decode("utf-8") .splitlines(True),
        #                  diff.b_blob.data_stream.read().decode("utf-8") .splitlines(True),
        #                  'Original', 'Current')),
        #     end="")
        lines = list(context_diff(diff.a_blob.data_stream.read().decode("utf-8").splitlines(True),
                                  diff.b_blob.data_stream.read().decode("utf-8").splitlines(True),
                                  'Original', 'Current'))
    for line in lines:
        pass
    pprint(lines)
