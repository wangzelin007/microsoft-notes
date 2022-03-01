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