import seaborn as sns
import pandas as pd
import pysnooper

data=sns.load_dataset('iris')

def slow():
    class_list = list()
    for index, data_row in data.iterrows():
        petal_length = data_row[ 'petal_length' ]
        class_num = compute_class(petal_length)
        class_list.append(class_num)


def compute_class(petal_length):
    if petal_length<=2:
        return 1
    elif 2<petal_length<5:
        return 2
    else:
        return 3

@pysnooper.snoop()
def text():
        slow()

        data.apply(lambda row:compute_class(row['petal_length']),axis=1)

        pd.cut(x=data.petal_length,bins=[0,2,5,100],include_lowest=True,labels=[1,2,3]).astype(int)

text()

#pandas 尽量不要用for循环，使用apply会提升5倍时间左右，因为apply()内部
#会遍历Cython迭代器.如果使用Cpython处理过的函数,apply()会更快