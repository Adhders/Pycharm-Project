import packA.a1  #packA不能省去，因为a1中有相对路径
import packA.subA.sa2
import packA.packC.d
import math
import sys
import packA
print(packA)
import time  #导入的是系统的time

time.time()
packA.packA_func()
packA.a1_func()
packA.a1.a1_func()
print(sys.path)
from packA.subA.sa1 import hellowWorld
hellowWorld()