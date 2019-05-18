import time
import functools

def clock(func):

    # functools.wraps(func)装饰器的作用是将func函数的相关属性复制到clock中
    # 比如说__name__, __doc__等等

    @functools.wraps(func) #去掉并无显著影响
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        time.sleep(0.000000001) #重复使用time.time()会导致时间重复
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(str(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print ('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result  #调用的函数仍带修饰器

    return clocked



#@functools.lru_cache()
@clock
def fibonacci(n):
    #time.sleep(0.01)
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
   print(fibonacci(5))