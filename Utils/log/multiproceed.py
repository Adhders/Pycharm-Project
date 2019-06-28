import multiprocessing as mp
from multiprocessing import Pool, Manager
from itertools import repeat
from functools import partial
import sys
import re
import os
import time
import datetime
#参考https://blog.csdn.net/jeffery0207/article/details/82958520
l = mp.Lock()  # 定义一个进程锁
v = mp.Value('i', 0)  # 定义共享内存
import logging

from logging import getLogger, Formatter
from cloghandler import ConcurrentRotatingFileHandler

try:
    import codecs
except ImportError:
    codecs = None

class MultiprocessHandler(logging.FileHandler):
    """支持多进程的TimedRotatingFileHandler"""
    def __init__(self,filename,when='D',backupCount=0,encoding=None,delay=False):
        """filename 日志文件名,when 时间间隔的单位,backupCount 保留文件个数
        delay 是否开启 OutSteam缓存
            True 表示开启缓存，OutStream输出到缓存，待缓存区满后，刷新缓存区，并输出缓存数据到文件。
            False表示不缓存，OutStrea直接输出到文件"""
        self.prefix = filename
        self.backupCount = backupCount
        self.when = when.upper()
        # 正则匹配 年-月-日
        self.extMath = r"^\d{4}-\d{2}-\d{2}"

        # S 每秒建立一个新文件
        # Motion 每分钟建立一个新文件
        # H 每天建立一个新文件
        # D 每天建立一个新文件
        self.when_dict = {
            'S':"%Y-%m-%d-%H-%Motion-%S",
            'Motion':"%Y-%m-%d-%H-%Motion",
            'H':"%Y-%m-%d-%H",
            'D':"%Y-%m-%d"
        }
        #日志文件日期后缀
        self.suffix = self.when_dict.get(when)
        if not self.suffix:
            raise ValueError(u"指定的日期间隔单位无效: %s" % self.when)
        #拼接文件路径 格式化字符串
        self.filefmt = os.path.join("logs","%s.%s" % (self.prefix,self.suffix))
        #使用当前时间，格式化文件格式化字符串
        self.filePath = datetime.datetime.now().strftime(self.filefmt)
        #获得文件夹路径
        _dir = os.path.dirname(self.filefmt)
        try:
            #如果日志文件夹不存在，则创建文件夹
            if not os.path.exists(_dir):
                os.makedirs(_dir)
        except Exception:
            print (u"创建文件夹失败")
            print (u"文件夹路径：" + self.filePath)
            pass

        if codecs is None:
            encoding = None

        logging.FileHandler.__init__(self,self.filePath,'a+',encoding,delay)

    def shouldChangeFileToWrite(self):
        """更改日志写入目的写入文件
        :return True 表示已更改，False 表示未更改"""
        #以当前时间获得新日志文件路径
        _filePath = datetime.datetime.now().strftime(self.filefmt)
        #新日志文件日期 不等于 旧日志文件日期，则表示 已经到了日志切分的时候
        #   更换日志写入目的为新日志文件。
        #例如 按 天 （D）来切分日志
        #   当前新日志日期等于旧日志日期，则表示在同一天内，还不到日志切分的时候
        #   当前新日志日期不等于旧日志日期，则表示不在
        #同一天内，进行日志切分，将日志内容写入新日志内。
        if _filePath != self.filePath:
            self.filePath = _filePath
            return True
        return False

    def doChangeFile(self):
        """输出信息到日志文件，并删除多于保留个数的所有日志文件"""
        #日志文件的绝对路径
        self.baseFilename = os.path.abspath(self.filePath)
        #stream == OutStream
        #stream is not None 表示 OutStream中还有未输出完的缓存数据
        if self.stream:
            #flush close 都会刷新缓冲区，flush不会关闭stream，close则关闭stream
            #self.stream.flush()
            self.stream.close()
            #关闭stream后必须重新设置stream为None，否则会造成对已关闭文件进行IO操作。
            self.stream = None
        #delay 为False 表示 不OutStream不缓存数据 直接输出
        #   所有，只需要关闭OutStream即可
        if not self.delay:
            #这个地方如果关闭colse那么就会造成进程往已关闭的文件中写数据，从而造成IO错误
            #delay == False 表示的就是 不缓存直接写入磁盘
            #我们需要重新在打开一次stream
            #self.stream.close()
            self.stream = self._open()
        #删除多于保留个数的所有日志文件
        if self.backupCount > 0:
            print ('删除日志')
            for s in self.getFilesToDelete():
                print (s)
                os.remove(s)

    def getFilesToDelete(self):
        """获得过期需要删除的日志文件"""
        #分离出日志文件夹绝对路径
        #split返回一个元组（absFilePath,fileName)
        #例如：split('I:\ScripPython\char4\mybook\util\logs\mylog.2017-03-19）
        #返回（I:\ScripPython\char4\mybook\util\logs， mylog.2017-03-19）
        # _ 表示占位符，没什么实际意义，
        dirName,_ = os.path.split(self.baseFilename)
        fileNames = os.listdir(dirName)
        result = []
        #self.prefix 为日志文件名 列如：mylog.2017-03-19 中的 mylog
        #加上 点号 . 方便获取点号后面的日期
        prefix = self.prefix + '.'
        plen = len(prefix)
        for fileName in fileNames:
            if fileName[:plen] == prefix:
                #日期后缀 mylog.2017-03-19 中的 2017-03-19
                suffix = fileName[plen:]
                #匹配符合规则的日志文件，添加到result列表中
                if re.compile(self.extMath).match(suffix):
                    result.append(os.path.join(dirName,fileName))
        result.sort()

        #返回  待删除的日志文件
        #   多于 保留文件个数 backupCount的所有前面的日志文件。
        if len(result) < self.backupCount:
            result = []
        else:
            result = result[:len(result) - self.backupCount]
        return result

    def emit(self, record):
        """发送一个日志记录
        覆盖FileHandler中的emit方法，logging会自动调用此方法"""
        try:
            if self.shouldChangeFileToWrite():
                self.doChangeFile()
            logging.FileHandler.emit(self,record)
        except (KeyboardInterrupt,SystemExit):
            raise
        except:
            self.handleError(record)

log_path="./log"
log_filename='thread.log'

def create_logger(log_path=os.getcwd(),  # 存放日志的目录
                  level=logging.DEBUG,
                  formatter=logging.BASIC_FORMAT,  # 日志输出格式
                  logger_name="",  # 可以使用logging.getlogger(logger_name)使用此logger
                  mode='a',
                  delay=0,
                  debug=True,
                  log_filename=log_filename,  # 保存日志的文件名（备份出的文件会以此名+.1、 .2命名）
                  encoding=None,
                  maxBytes=50,  # 每个日志文件的最大容量
                  backupCount=3 ):
    if not os.path.exists(log_path):
        os.mkdir(log_path)
        # 存放log的文件名
    log_filename = os.path.join(log_path, log_filename)

    # 创建一个logger
    logger = logging.getLogger(logger_name)
    # 设置日志等级
    logger.setLevel(level)
    # 创建一个滚动日志处理器
    crfh = ConcurrentRotatingFileHandler(log_filename, mode=mode, maxBytes=maxBytes, backupCount=backupCount, delay=delay,
                                         debug=debug, encoding=encoding)
    # 定义handler的输出格式
    # 设定日志输出格式
    crfh.setFormatter(formatter)
    # 添加日志处理器
    logger.addHandler(crfh)
    # 返回logger对象
    return logger




# 日志格式
formatter_log = logging.Formatter('%(asctime)s - %(filename)s [line: %(lineno)d] 【%(levelname)s】 ----- %(message)s')
# 生成一个logger
logger = create_logger(log_path=log_path, logger_name="mylogger", formatter=formatter_log)



def func(a, b):
    return a + b
def foo(a):
    print(a)
def main():
    a_args = [1,2,3]
    second_arg = 1
    with Pool() as pool:
        L = pool.starmap(func, [(1, 1), (2, 1), (3, 1)])
        M = pool.starmap(func, zip(a_args, repeat(second_arg)))
        N = pool.map(partial(func, b=second_arg), a_args)
        assert L == M == N
        print(L,M,N)



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

    # p1 = mp.Process(target=job, args=(1))    # 需要将lock传入
    # p2 = mp.Process(target=job, args=(3))
    #
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    with mp.Pool(processes=4, maxtasksperchild=None) as pool:
        pool.starmap(job,zip(range(1,3),repeat(2)))
        pool.close()
        pool.join()

def func(dic, c):

    dic['count'] += c


if __name__ == "__main__":
    multicore()


#     d = Manager().dict()#使用 multiprocessing.Manager 来创建对象，这样的对象可以被共享,Manager() 内部有加锁机制，不允许
#     # 两个进程同时修改一份数据，因为进程的数据是独立的，因此数据是安全的。
#     # Manager对象支持的对象包括list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier,
#     # Queue, Value 以及 Array
#
#
#     # d = dict() 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，
#     # 所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改
#     d['count'] = 0
#     args = [(d, 1), (d, 2), (d, 3)]
#     pool = Pool(3)
#     pool.starmap(func, args)#starmap与map的区别是starmap可以传进去多个参数
#     pool.close()
#     pool.join()
#     print(f'dic={d}')










