70 -> 50 
开启测试时间记录--duration=0，对速度大于10s的测试逐个排查原因并修复 PR：
50 -> 25
pytest 开启并行 gw - group worker
   pytest -n auto
   With this call, pytest will spawn a number of workers processes equal to the number of available CPUs, and distribute the tests randomly across them.
25 -> 7
pipeline 将所有测试切分为8个任务，为什么是8个，经过多次测试，少了会变慢，多了会分两次执行。 
每个任务中的module自动分配，保证每个task里面执行时间接近，同时开始，同时结束。