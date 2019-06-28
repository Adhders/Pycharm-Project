import pysnooper

def run():
    a=1
    print(a)
#@pysnooper.snoop(depth=2) #显示函数内部调用函数的snoop行
def number_to_bits(number):
    if number:
        bits = []
        with pysnooper.snoop(depth=2):
            run()
            while number:
                number, remainder = divmod(number, 2)
                bits.insert(0, remainder)
            return bits
    else:
        return [0]

number_to_bits(6)