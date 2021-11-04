# import signal
import timeout_decorator

# class TimeoutError(Exception):
#     def __init__(self, msg):
#         super(TimeoutError, self).__init__()
#         self.msg = msg


# windows 不支持
# def time_out(interval, callback):
#     def decorator(func):
#         def handler(signum, frame):
#             raise TimeoutError("run func {func.__name__} timeout")
#
#         def wrapper(*args, **kwargs):
#             try:
#                 signal.signal(signal.SIGALRM, handler)
#                 signal.alarm(interval)
#                 result = func(*args, **kwargs)
#                 signal.alarm(0)
#                 return result
#             except TimeoutError as e:
#                 callback(e)
#
#         return wrapper
#
#     return decorator


# def callback_func(e):
#     print(e.msg)


# @time_out(3, callback_func)
@timeout_decorator.timeout(3)
def test_timeout():
    import time
    # time.sleep(4)
    cnx = {'a': 'b'}
    return cnx


def test_timeout_fa():
    ref = test_timeout()
    print(ref)


def write_db():
    import mysql.connector
    print('Connect DB...')
    # Connect
    cnx = mysql.connector.connect(user='fey@clisqldbserver',
                                  password='pwd',
                                  host='clisqldbserver.mysql.database.azure.com',
                                  port=3306,
                                  database='clidb',
    )
    print('Connect DB Success')

if __name__ == '__main__':
    # write_db()
    test_timeout_fa()