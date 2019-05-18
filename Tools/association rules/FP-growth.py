import fp_growth as fpg
import re
import xlwt
set=[]
foo=open('frequency.txt','r',encoding='utf-8')
for text in foo.readlines():
    word=re.split('\s+',text.strip())
    set.append(word)


frequent_itemsets = fpg.find_frequent_itemsets(set, 1, include_support=True)
frequent=[]
for key,num in frequent_itemsets:
    frequent.append((key,num,len(key)))

sorted_frequent=sorted(frequent,key=lambda x:(x[2], -x[1]),reverse=True) # '-'负号表示逆序排序

f = xlwt.Workbook()
sheet1 = f.add_sheet('frequency_4', cell_overwrite_ok=True)

count_1=0
count_2=0
count_3=0
count_4=0
count_5=0
count_6=0

foo=open('frequency_mode.txt','w',encoding='utf-8')
count=0
for kenal,num,length in sorted_frequent:
    if len(kenal)>=6:
        count_6 +=1
    elif len(kenal)>=5:
        count_5 +=1
    elif len(kenal)>=4:
        count_4 +=1
    elif len(kenal)>=3:
        count_3 +=1
    elif len(kenal)>=2 :
         count_2 +=1
    else:
        count_1 +=1
    model=' '.join(kenal)
    foo.writelines(model+'\n')
print(count_1,count_2,count_3,count_4,count_5,count_6)

