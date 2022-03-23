import time

import multiprocessing

# 设置回调函数
def setcallback(x):
    with open('test_write_file1.txt', 'a+') as f:
        line = str(x) + "\n"
        f.write(line)

def multiplication(num):
    return num*(num + 1)

def write_to_file(x):
    with open('test_write_file2.txt', 'a+') as f:
        x = x * (x + 1)
        line = str(x) + "\n"
        f.write(line)

def func1():
    pool = multiprocessing.Pool(6)
    for i in range(1000):
        pool.apply_async(func=multiplication, args=(i,), callback=setcallback)
    pool.close()
    pool.join()

def func2():
    pool = multiprocessing.Pool(6)
    pool.imap_unordered(write_to_file, range(1000))
    pool.close()
    pool.join()

if __name__ == '__main__':
    func1()
    func2()
