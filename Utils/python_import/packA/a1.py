print('import other module in packA/a1.py')
import other #(绝对导入)
from . import a2
import packA.subA.sa1

from . import a2
from .subA import sa1
# from packA import other # This is invalid

def a1_func():
    print("running a1_func()")
