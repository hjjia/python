# -*- coding: utf-8 -*-
from xlrd import open_workbook
from xlutils.copy import copy
import os

def editExl(path, name):
    if os.path.exists('/data'):
        os.removedirs("/data")
    # 括号里放入要读取的文件的绝对路径,相对路径也可以 
    # os.getcwd() 返回当前.py文件所在的绝对路径
    print(os.getcwd(), 'lujing')
    wb = open_workbook(path + '/' + name)
    # 获取所读取文件的第一张表单
    # sheet = wb.sheet_by_index(0)
    # 获取该表单的行数
    # s = sheet.nrows

    # 获取当前文件的工作表（sheet）list
    sheetList = wb.sheets()
    # print('sheetList', sheetList)

    # 复制原文件，因为原文件只能读取，不能写入数据，所以要复制得到一个可以写入数据的文件
    newwb = copy(wb)
    sheetIndex = 0
    for sheet in sheetList:

        # 获取可写文件的第一张表单
        newsheet = newwb.get_sheet(sheetIndex)
        print(newsheet, newsheet.get_rows())
        index = 0
        try:
            for row in sheet.get_rows():
                # 遍历每一行，当8列的值小于12时，就把该值改为0
                print(row)
                print(row[0].value, '000000000000000')
                if row[0].value < 12:
                    print('here', index)
                    # newsheet.write(index, 0, 0)
                    print('after here')
                index = index + 1
        except:
            print("aaa")
        sheetIndex = sheetIndex + 1

    mkdir('./data')
    newwb.save('./data/' + name)

def mkdir(path): 
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print('--- folder mk ---')
    else:
        print('--- folder exists ---')

def getFileList(path):
    return os.listdir(path)

def editAll():
    originPath = './origin'
    fileList = getFileList(originPath)
    print(fileList)
    for fileItem in fileList:
        editExl(originPath, fileItem)
editAll()
# editExl('', '')