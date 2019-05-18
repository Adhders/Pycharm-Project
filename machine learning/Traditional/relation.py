import gensim.models.word2vec as w2v
import xlrd
import xlwt
import numpy as np
import re
model=w2v.Word2Vec.load('insurance.model')

def relation(path):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('test', cell_overwrite_ok=False)
    sheet2 = f.add_sheet('relation',cell_overwrite_ok=False)
    data = xlrd.open_workbook(path)
    sh = data.sheet_by_name("test")
    a=np.zeros(sh.nrows)
    print(sh.nrows)
    for n in range(1,2):
        text_n=re.split('\s+',sh.cell_value(n,0).strip())
        for m in range(n,n+1):
            text_m=re.split('\s+',sh.cell_value(m,0).strip())

            score=model.similarity('健康险','')#model.similarity 计算两个单词间的相似度
            print(score)
            if score>0.9:
                a[n]=a[n]+1
                a[m]=a[m]+1
                print(m,score)

        # sheet1.write(n,4,a[n])

    f.save('text_new.xls')

path='text.xls'
relation(path)

