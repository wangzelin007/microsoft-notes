python
装饰器：就是利用了闭包的原理，所以我们说装饰器就是是闭包也是完全没有问题的。
闭包：一个函数和对其周围状态（lexical environment，词法环境）的引用捆绑在一起（或者说函数被引用包围），这样的组合就是闭包（closure）。
     内部函数可以访问函数外面的变量。
引用计数：python根据变量的引用计数来判断是变量是否需要回收。
当一个对象的引用被创建或复制时，对象的引用计数加1；当一个对象的引用被销毁时，对象的引用计数减1，如果对象的引用计数减少为0，将对象的所占用的内存释放。
闭包是因为对象的引用一直没有被销毁引用计数不为0，所以在inner函数里一直可以访问对象的值。
property 装饰器: 用于类中的函数，使得我们可以像访问属性一样来获取一个函数的返回值。

内存管理机制：引用计数 & 标记消除和分代回收（解决循环引用）
标记消除：当两个对象的引用计数同时为1，且只存在它们两个之间的循环引用，那么这两个对象要被回收
分代回收：分代回收是为了更合理的调用标记消除而存在的，具体实现如下
1. 新创建的对象为0代
2. 每进行一次标记消除，该存活对象的代数+1
3. 代数越高的对象，进行标记消除的间隔时间（阈值）越长

Python 的内存管理的优化方法?
手动进行垃圾回收
调高垃圾回收阈值
避免循环引用（手动解循环引用和使用弱循环）

如何避免内存泄漏？
循环引用是导致内存泄漏的主要元凶，以此可以
1. 使用del来删除不再使用的对象实体，可以解决绝大部分内存泄漏问题
2. 使用python的扩展模块gc来查看不能回收对象的详细信息
3. 使用sys.getrefcount(obj)来查看对象的引用计数次数，根据返回值判断是否存在内存泄漏

数据结构：
队列
队列中的数据元素遵循“先进先出”（First In First Out）的原则，简称FIFO结构；
在队尾添加元素，在队头删除元素。
栈
栈中的数据元素遵守”先进后出"(First In Last Out)的原则，简称FILO结构。
限定只能在栈顶进行插入和删除操作。

基础：
[TCP && UDP](https://leetcode-cn.com/circle/discuss/b4PW9S/)
[HTTP](https://leetcode-cn.com/circle/discuss/cxn9hV/)
计算机网络分层

数据库：
事务 ACID 原子性atomicity 一致性consistency 隔离性isolation 持久性durability
Mysql Innodb 索引数据结构
Mysql 如何通过索引快速查找数据的
为什么不能使用select * 

正则表达式：
https://regex101.com/
**test1**
self.cmd('az vm create -n')
test.cmd("az vm create -n")
self.vm_cmd(f'az vm create -n')
**az vm create -n**
r'.\w{0,}cmd\(f?(?:\'|")(.*)(?:\'|")\)'
**test2**
2021-12-29
02021-12-29
2021-12-42
**yyyy-mm-dd**
reg = r'^\d{4}-(?:1[0-2]|0?[1-9])-(?:[12]\d|3[01]|0?[1-9])$'

算法题
关注测试怎么写！
1. 二叉树的前序遍历
2. 二叉树锯齿形层序遍历
3. 链表两两翻转再倒叙

Linux:
find . -type f -name "*.py" 查找文件
tar -czvf docker.tar.gz docker/ [create,gzip,verbose,file]
tar xvf source.tar.gz [extract,verbose,file]
sed -e '1,10s/enchantment/entrapment/g' myfile2.txt 在第一到第十行上替换

Git 使用：
如何暂存代码 git stash
提交代码时应该包含那些信息：
1. 描述这个提交包含那些内容
2. 如果是为了解决一些问题，关联的问题链接等等。
3. 风险提示
4. 测试提示
5. 使用方法
6. 一些必要的截图等等。