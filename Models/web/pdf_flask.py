from flask import Flask ,request
import shutil
import fitz
import zipfile
import os
import argparse


app = Flask(__name__)


@app.route('/')
def split_zip():
    path=request.args.get('path')
    name=request.args.get('name')

# http://127.0.0.1:9000/?name=JUNBOLI&path=C:\\Users\\junbo\\Desktop\\Drawings%20Demo\\test.pdf

    doc = fitz.open(path)
    count = doc.pageCount
    num=0
    if os.path.exists('./download/%s'%name):
        shutil.rmtree('./download/%s'%name)
    os.makedirs('./download/%s'%name)
    while num<count:
        doc2=fitz.open()
        doc2.insertPDF(doc,num,num)
        path=os.path.join('./download/',name,''.join([name,'_',str(num+1),'.pdf']))
        doc2.save(path, garbage=4, deflate=1)
        num=num+1
    with zipfile.ZipFile('./download/%s.zip'%name, 'w') as z:
        for d in os.listdir('./download/%s' %name):
            fullpath=os.path.join('./download/%s' %name,d)
            z.write(fullpath,d)
    shutil.rmtree('./download/%s' % name)
    return './download/%s.zip'%name


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=9000, type=int)
    args = parser.parse_args()
    app.run('0.0.0.0', args.port)

if __name__=='__main__':
    main()


