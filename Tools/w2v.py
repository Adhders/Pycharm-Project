#!/user/bin/python
#coding:utf-8
__author__ = 'junbo'
from gensim.corpora import WikiCorpus

import codecs
import re
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import multiprocessing
# from langconv import * #繁体字转为简体字

'''
读取中文wiki语料库，并解析提取xml中的内容

wiki 语料库下载来源英文 https://dumps.wikimedia.org/enwiki/latest/  
中文https://dumps.wikimedia.org/zhwiki/latest/

'''
def dataprocess(path=r'C:\Users\junbo\Desktop\wiki\enwiki-latest-pages-articles-multistream-index.txt.bz2'):
    i=0
    output=open('zh_wiki.txt','w',encoding='utf-8')
    wiki=WikiCorpus(fname=path,lemmatize=False,dictionary={})
    for text in wiki.get_texts():
        output.write(" ".join(text)+'\n')
        i=i+1
        if(i%10000==0):
            print('Saved '+str(i)+' articles')
    output.close()
    print('Finished Saved '+str(i)+' articles')


def segment_text(source_corpus, train_corpus):
    '''
    切词,去除标点符号
    :param source_corpus: 原始语料
    :param train_corpus: 切词语料
    :param punctuation: 去除的标点符号
    :return:
    '''
    # 严格限制标点
    strict_punctuation = '。，、＇：∶；?‘’“”〝〞ˆˇ﹕︰﹔﹖﹑·….¸;！´？！～—ˉ｜‖＂〃｀@﹫﹟#﹩$﹠&﹪%*﹡﹢﹦﹤‐¯―﹨ˆ˜+=<-\ˇ~（）〈〉‹›﹛﹜『』［］《》〔〕{}「」【】'
    # 简单限制标点符号
    simple_punctuation = '’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    # 去除标点符号
    punctuation = simple_punctuation + strict_punctuation
    with open(source_corpus, 'r', encoding='utf-8') as f, open(train_corpus, 'w', encoding='utf-8') as w:
        for line in f:
            # 去除标点符号
            line = re.sub('[{0}]+'.format(punctuation),' ', line)
            # 切词
            words = re.split(' ',line)
            w.write(''.join(words))




'''
opencc繁体转简体，jieba中文分词
'''
# def trans_seg(source, train):
#     with codecs.open(train,'w','utf-8') as wopen:
#         print('开始...')
#         with codecs.open(source,'r','utf-8') as ropen:
#             while True:
#                 line=ropen.readline().strip()
#                 if not line and not ropen.readline().strip():
#                     break
#                 text=re.sub('[^\u4e00-\u9fa5]','',line)
#                 #char = Converter('zh-hans').convert(char)
#                 words=jieba.cut(text)
#                 seg=''
#                 for word in words:
#                     if len(word)>1 : #去掉长度小于1的词和英文
#                         seg+=word+' '
#                 wopen.write(seg+'\n')
#     print('结束!')


def delete(source,output):
    deletion=set()
    with open('nonsense_2.txt','r',encoding='utf-8')  as foo:
        for line in foo.readlines():
            deletion.add(line.strip())


    with open(source,'r',encoding='utf-8') as f,open(output,'w',encoding='utf-8') as g:
        for line in f.readlines():
            string=set()
            for text in re.split('\s+',line.strip()):
                # text=re.sub('[0-9]','',text)
                if len(text)>=2:
                    if text in deletion:
                        continue
                    string.add(text)
            strings=' '.join(list(string))
            g.write(strings+'\n')




'''
利用gensim中的word2vec训练词向量
'''
def word2vec():
    print('Start...')
    rawdata='insurance_segmented.txt'
    modelpath='insurance.model'
    #vectorpath='vector'
    model=Word2Vec(LineSentence(rawdata),size=100,window=5,min_count=2,workers=multiprocessing.cpu_count())#参数说明，gensim函数库的Word2Vec的参数说明
    model.save(modelpath)
    #model.wv.save_word2vec_format(vectorpath,binary=False)
    print("Finished!")

def wordsimilarity():
    model=Word2Vec.load('modeldata.model')
    semi=''
    try:
        semi=model.most_similar('保险',topn=10)#python3以上就不需要decode
    except KeyError:
        print('The word not in vocabulary!')

    #print(model[u'日本'])#打印词向量
    for term in semi:
        print('%s,%s' %(term[0],term[1]))


if __name__=='__main__':
    dataprocess()
    #trans_seg('insurance.txt','insurance_segmented.txt')
    #word2vec()
    #delete('question.txt','user_dict.txt')
    #wordsimilarity()
    #segment_text('insurance.txt','insurance.txt')
