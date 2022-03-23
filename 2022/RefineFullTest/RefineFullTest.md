pytest --durations=3 --durations 接收一个整型值 n，并报告最慢的 n 个测试。

[pytest]
norecursedirs = docs *.egg-info .git appdir .tox

call with test path: pytest src/www/tests/

adding PYTHONDONTWRITEBYTECODE=1
Windows Batch: set PYTHONDONTWRITEBYTECODE=1
Unix: export PYTHONDONTWRITEBYTECODE=1
subprocess.run: Add keyword env={'PYTHONDONTWRITEBYTECODE': '1'}

upgrade pytest version

generate dependencies map
only run dependencies map test cases

分配算法
修改顺序
拆task

azdev test hdinsight --live --mark serial --xml-path test_results.sequential.xml --no-exitfirst -a "-n 1 --json-report --json-report-summary --json-report-file=hdinsight.report.sequential.json --html=hdinsight.report.sequential.html --self-contained-html --reruns 3 --capture=sys"

azdev test hdinsight --live --mark "not serial" --xml-path test_results.parallel.xml --no-exitfirst -a "-n 8 --json-report --json-report-summary --json-report-file=hdinsight.report.parallel.json --html=hdinsight.report.parallel.html --self-contained-html --reruns 3 --capture=sys"
->
azdev test hdinsight --live --mark "not serial" --xml-path test_results.parallel.xml --no-exitfirst -a "-n 8 --capture=sys"
->
azdev test hdinsight --live --mark "not serial" --xml-path test_results.parallel.xml --no-exitfirst -a "-n 8 --capture=sys --durations=0"

增加一个 rebase 的命令即可

已经有对比了
azdev test --no-exitfirst --repo=./ --src=HEAD --tgt=origin/dev --cli-ci --profile latest --verbose --series

自动变基
git config --global pull.rebase true
git config --global rebase.autoStash true

full test 顺序调整 TODO

azdev test --no-exitfirst --repo=./ --src=HEAD --tgt=origin/dev --cli-ci --profile latest --verbose --series -a "-n 4 --durations=10"
C:\Code\azure-cli-dev-tools\azdev\operations\testtool\__init__.py +149

优化diff
https://github.com/Azure/azure-cli/pull/21711 ys
https://github.com/Azure/azure-cli/pull/21643 
https://github.com/Azure/azure-cli/pull/21698
https://dev.azure.com/azure-sdk/public/_build/results?buildId=1449925&view=logs&j=74095127-2a27-5370-37ed-15a4193f243f&t=5cf5f89a-09fb-583c-72e4-4e4427c89fb1

if any(core_package in modified_packages for core_package in ['core', 'testsdk', 'telemetry']):
# tests under all packages    

ERROR: usage error, invalid branch: upstream/dev

pull dev
git checkout dev
git pull
rebase feature 
git checkout $(System.PullRequest.SourceBranch)
git rebase dev

if parallel:
    arguments += ['-n', 'auto']

1. 分多台机器同时跑
2. 每台机器上也要开并行 (需要解决并行冲突的问题: 1.同时写一个本地文件。 是否可以通过查找with open 分析 345 处)
3. 是否还有其他历史原因
4. 为什么会产生测试依赖的问题？ 比如创建vm需要创建网络，或者多个用例同时创建了vm，为什么就会冲突，冲突的点在哪里？
   是否是因为测试写的不标准，比如使用了同样的vm名称，网络信息导致的冲突? 是否可以通过规范测试用例来解决？
   否则只能禁用并行化测试了。

今天还有一个很关键，反复跑，看是否出现问题。
先不纠结live test。