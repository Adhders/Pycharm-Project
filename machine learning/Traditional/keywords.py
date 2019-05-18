import jieba.analyse
import jieba.posseg as pseg
jieba.load_userdict('user_dict.txt')
import time

# words=pseg.cut(s)
# for w in words:
#     if w.flag.startswith('n'):
#         print(w.word,w.flag)
#
# for x, w in jieba.analyse.textrank(s, withWeight=False):
#      print('%s %s' % (x, w))

#
from jieba import analyse
tfidf = analyse.extract_tags
# string='什么是新农合保险？农村合作医疗补偿政策'
# keywords = tfidf(string,withWeight=True,allowPOS=('ns','n','nd','nh','nl','ns','nt','nz','i','j',),withFlag=True)
# for key in keywords:
#     print(key)

def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

primary=set()
stop_list=stopwordslist('stop_words.txt')
with open('keywords.txt','w',encoding='utf-8') as f:
    with open('question.txt','r',encoding='utf-8') as g:
        for string in g.readlines():
            string=string.strip()
            keywords = tfidf(string,withWeight=False,allowPOS=('ns','n','nd','nh','nl','ns','nt','nz','i','j'),withFlag=False)
            str=[]
            for key in keywords:
                if key in stop_list:
                    continue
                str.append(key)
            if len(str):
                primary.add(str[0])

            f.writelines(' '.join(str)+'\n')

with open('primary_word.txt','w',encoding='utf-8') as foo:
    for word in list(primary):
         foo.writelines(word+'\n')