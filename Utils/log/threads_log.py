
from itertools import repeat
import time
import logging.config
import multiprocessing as mp
from multiprocessing import Pool, Manager
import concurrent_log_handler  #解决windows logging 的多线程运行问题
from simple_settings import settings #simple_setting 实在控制行运行的
from simple_settings import LazySettings
import os

"""  Although logging is thread-safe, and logging to a single read from multiple threads
     in a single process is supported, logging to a single read from multiple processes is not
     supported, because there is no standard way to serialize access to a single read across
     multiple processes in Python."""

# logging.config.fileConfig("logger.conf")
# logger = logging.getLogger('cse.log')

l = mp.Lock()  # 定义一个进程锁
v = mp.Value('i', 0)  # 定义共享内存
#os.environ['SIMPLE_SETTINGS'] = 'settings.development.py'添加环境变量
settings = LazySettings('settings.development')
# settings.setup()  可以省略
logging.config.dictConfig(settings.LOGGING_CONFIG)
logger = logging.getLogger('my_project')


def job(num,a):
    l.acquire()
    # 锁住
    for _ in range(10):
        time.sleep(0.1)
        v.value += num  # 获取共享内存
        logger.debug(v.value)

    l.release()  # 释放

def multicore():
    manager = mp.Manager()
    q = manager.Queue()
    with mp.Pool(processes=4, maxtasksperchild=None) as pool:
        pool.starmap(job,zip(range(1,3),repeat(2)))
        pool.close()
        pool.join()

def func(dic, c):

    dic['count'] += c


if __name__ == "__main__":
    logger.error("error")
    multicore()

for idx in range(0, 10):
    logger.debug('%d > A debug message' % idx)

# logger.debug("error")
# logger.error("error")
# logger.error("abc")
# logger.info('Hello')


