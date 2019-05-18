import random
import numpy as np
import os
import cv2
import fitz
from tqdm import tqdm
from scipy.ndimage import filters
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('song','C:\\Users\\junbo\\Desktop\\arial narrow.ttf'))
from reportlab.platypus import Paragraph,SimpleDocTemplate
from reportlab.lib import  colors
from PIL import Image
import shutil


def generator(element,Max_len):

    text=random.sample(mixtion,Max_len)
    text=u''.join(text)
    try:
        labels=['%d ' %element.index(i) for i in text]
    except ValueError:
        text=random.sample(remain,Max_len)
        labels = ['%d ' %element.index(i) for i in text]
    finally:
        return text ,labels

def gaussian_noise(height, width):
    """
        Create a background with Gaussian noise (to mimic paper)
    """

    # We create an all white image
    image = np.ones((height, width)) * 255

    # We add gaussian noise
    cv2.randn(image, 250, 3)        #randn(dst, mean, stddev) -> dst

    return Image.fromarray(image).convert('L')

def jpg_make(path, save_dir):
    doc = fitz.open(path)
    page = doc[0]
    trans = fitz.Matrix(2,2)
    pix = page.getPixmap(matrix=trans, alpha=False)
    img = Image.frombytes("RGB", [ pix.width, pix.height ], pix.samples).convert('L')
    image = np.array(img, dtype=np.uint8)
    slice_image = image[160:192, 155:435]
    cv2.imwrite(save_dir,slice_image)




def samples(path,number,dict,max_label_length):
    with open(os.path.join(path,'labels.txt'),'w',encoding='utf-8') as f:
        for i in tqdm(range(number)):
            text, labels = generator(dict,max_label_length)
            Style = getSampleStyleSheet()

            bt = Style['Normal']  # 字体的样式
            bt.fontName = 'arial'  # 使用的字体

            t =random.randint(0, 2)

            # if choice==1:
            #     pdfmetrics.registerFont(TTFont('arial', 'C:\\Users\\junbo\\Desktop\\arialbd.ttf'))
            # elif choice==2:
            #     pdfmetrics.registerFont(TTFont('arial', 'C:\\Users\\junbo\\Desktop\\arialn.ttf'))
            # else:
            pdfmetrics.registerFont(TTFont('arial', 'C:\\Users\\junbo\\Desktop\\arial narrow.ttf'))
            bt.fontSize =random.randint(11,15)

            # bt.wordWrap = 'CJK'    #该属性支持自动换行，'CJK'是中文模式换行，用于英文中会截断单词造成阅读困难，可改为'Normal'
            bt.firstLineIndent = t #该属性支持第一行开头空格
            # bt.leading = 20             #该属性是设置行距

            labels.insert(0,'%d.jpg '%i)
            # save_dir = path + '{}.jpg'.format(i)
            # ##im=filters.gaussian_filter(im, kernel)
            ct=Style['Normal']
            ct.fontName='arial'
            #ct.fontSize=12
            ct.alignment=0            #居中
            ct.textColor = colors.black

            t = Paragraph(text,bt)
            os.makedirs('C:\\Users\\junbo\\Desktop\\train\\pdf')
            pdf=SimpleDocTemplate('C:\\Users\\junbo\\Desktop\\train\\pdf\\%d.pdf'%i)
            pdf.multiBuild([t])
            jpg_make('C:\\Users\\junbo\\Desktop\\train\\pdf\\%d.pdf'%i,'C:\\Users\\junbo\\Desktop\\train\\%d.jpg'%i)
            shutil.rmtree('C:\\Users\\junbo\\Desktop\\train\\pdf')
            f.writelines(labels + [ '\n' ])


if __name__=="__main__":

    mixtion = ['7', 'A','J', 'H', '5', 'Q', 'W', '4', 'K', 'O', '8', 'S','F',' ',
               'Z', '6','R', '9', '2', 'I', '&', 'X', 'G', 'N', '3', 'L','Y',' ',
               '1', 'V','B', 'P', 'E', 'Motion', 'T', 'D', 'C', 'U', '-', ' ','a',"'",
               'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n','o',
               'p', 'q','r','s','t','u','v','w','x','y','z','(','&', '_','.',',',
               ')', '0']

    remain = ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', '-', 'J', 'K', 'L', 'Motion', 'N', 'O']

    element=[]
    with open('C:\\Users\\junbo\\Desktop\\char_eng_94.txt','r') as g:
    #with open('char_eng_94.txt', 'r',encoding='utf-8') as g:
        for line in g.readlines():
            line=line.strip()
            element.append(line)
    element[-1]=' '

    samples('C:\\Users\\junbo\\Desktop\\train\\',100,element,15)
