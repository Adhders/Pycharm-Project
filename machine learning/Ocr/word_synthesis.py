import random
import numpy as np


import os
import cv2

from tqdm import tqdm
import sys

from scipy.ndimage import filters

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

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


def picture(height, width):
    """
        Create a background with a picture
    """

    pictures = os.listdir('C:\\Users\\junbo\\Desktop\\background')

    if len(pictures) > 0:
        picture = Image.open('C:\\Users\\junbo\\Desktop\\background/' + pictures[random.randint(0, len(pictures) - 1)])

        if picture.size[0] < width:
            picture = picture.resize([width, int(picture.size[1] * (width / picture.size[0]))], Image.ANTIALIAS)
        elif picture.size[1] < height:
            picture.thumbnail([int(picture.size[0] * (height / picture.size[1])), height], Image.ANTIALIAS)

        x = random.randint(0, picture.size[0] - width)
        y = random.randint(0, picture.size[1] - height)
        return picture.crop(
            (
                x,
                y,
                x + width,
                y + height,
            )
        )
    else:
       raise Exception('No images where found in the pictures folder!')

def gaussian_noise(height, width):
    """
        Create a background with Gaussian noise (to mimic paper)
    """

    # We create an all white image
    image = np.ones((height, width)) * 255

    # We add gaussian noise
    cv2.randn(image, 250, 3)        #randn(dst, mean, stddev) -> dst

    return Image.fromarray(image).convert('L')


def samples(path,number,dict,max_label_length):
    with open(os.path.join(path,'labels.txt'),'w',encoding='utf-8') as f:
        for i in tqdm(range(number)):
            text, labels = generator(dict,max_label_length)
            #im = Image.new("RGB", (280, 32), (255, 255, 255))

            noise=random.randint(0,3)

            if noise==0:
                im=gaussian_noise(32,280)
            else:
                im = picture(32, 280)

            dr = ImageDraw.Draw(im)

            t = random.randint(0, 3)
            choice=random.randint(1,4)

            if choice==1:
                n = random.randint(20, 26)
                m = random.randint(-2,1)
                font = ImageFont.truetype('C:\\Users\\junbo\\Desktop\\Arial.ttf', n)
            elif choice==2:
                n = random.randint(20, 26)
                m = random.randint(-2, 1)
                font = ImageFont.truetype('C:\\Users\\junbo\\Desktop\\arialn.ttf', n)
            else:
                n = random.randint(20, 26)
                m = random.randint(5, 8)
                font = ImageFont.truetype('C:\\Users\\junbo\\Desktop\\arial narrow.ttf', n)
            dr.text((t,m), text, font=font, fill="#00000000")
            labels.insert(0,'%d.jpg '%i)
            save_dir = path + '{}.jpg'.format(i)
            #im=filters.gaussian_filter(im, kernel)
            im.save(save_dir)
            f.writelines(labels + ['\n'])


def readfile(filename):
    with open(filename, 'r+') as f:
        lines = f.readlines()

        for line in lines:
            len=line.strip()
            len=len.split(' ')
            text=''.join(len)






if __name__=="__main__":

    if __name__ == "__main__":

        mixtion = [ '7', 'A', 'J', 'H', '5', 'Q', 'W', '4', 'K', 'O', '8', 'S', 'F', ' ',
                    'Z', '6', 'R', '9', '2', 'I', 'X', 'G', 'N', '3', 'L', 'Y', ' ', '1',
                    'V', 'B', 'P', 'E', 'Motion', 'T', 'D', 'C', 'U', '3', '4', "5", '7', '8',
                    '0']


        element = [ ]
        with open('C:\\Users\\junbo\\Desktop\\number.txt', 'r') as g:
            # with open('char_eng_94.txt', 'r',encoding='utf-8') as g:
            for line in g.readlines():
                line = line.strip()
                element.append(line)
        element[ -1 ] = ' '

        samples('C:\\Users\\junbo\\Desktop\\train\\', 100, element, 15)














    

