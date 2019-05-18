# -*- coding: utf-8 -*-
__author__ = "Li junbo"

from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger


def reader(filename, password):
    try:
        file = open(filename, 'rb')
    except IOError as err:
        print('failed to open the read' + str(err))
        return None
    pdf_reader = PdfFileReader(file, strict=False)
    if pdf_reader.isEncrypted:
        if password is None:
            print('%s haved been Encryed' % filename)
        else:
            if pdf_reader.decrypt(password) != 1:
                print('the password is unmatched')
            return None
    return pdf_reader


def spilt(filename, nums, password=None):
    """
    Spilt the read to nums pieces
    :param nums: the num should be spilt
    :param password: if need,enter the password
    """
    pdf_reader = reader(filename, password)
    if not pdf_reader:
        return
    if nums < 2:
        print("can't less 2 pages")
        return
    pages = pdf_reader.numPages
    if pages < nums:
        print('nums can\'t be more than pages')
        return
    each_pdf = pages // nums

    for num in range(1, nums + 1):
        pdf_writer = PdfFileWriter()
        split_pdf_name = "".join(filename)[:-4] + '_' + str(num) + '.pdf'
        start = each_pdf * (num - 1)
        end = each_pdf * num if num != nums else pages
        for i in range(start, end):
            pdf_writer.addPage(pdf_reader.getPage(i))
        pdf_writer.write(open(split_pdf_name, 'wb'))


def merger(filelist, merged_name, passwords=None):
    """
    merged the files in filelist
    :param merged_name: the filename after mergered
    :param passwords:
    :return:
    """
    filenums = len(filelist)
    pdf_merger = PdfFileMerger(False)

    for i in range(filenums):
        if passwords is None:
            password = None
        else:
            password = passwords[i]
        pdf_reader = reader(filelist[i], password)
        if not pdf_reader:
            return
        pdf_merger.append(pdf_reader)

    pdf_merger.write(open(merged_name, 'wb'))

if __name__=='__main__':
    filelist=[r'C:\\Users\\junbo\\Desktop\\Drawings Demo\\SM-MC-AR-081_1.pdf',
              r'C:\\Users\\junbo\\Desktop\\Drawings Demo\\SM-MC-AR-081_24.pdf',


              ]
    #spilt('C:\\Users\\junbo\\Desktop\\Drawings Demo\\SM-MC-AR-081.pdf',24)
    merger(filelist,'SM-MC-AR-007.pdf')
