# -*- coding: utf-8 -*-
import os
import xlwings as xw

def editExlXL(app, originPath, fileItem):
    # 打开已经有的工作薄(支持相对路径和绝对路径)
    wb = app.books.open(originPath + '/' + fileItem)

    # 获取第一个sheet
    sht = wb.sheets[0]

    # print(sht, 'sheet')

    # 修改a1的值
    # sht.range('a1').value = ''
    for sheet in wb.sheets:
        for picture in sheet.pictures:
            height = picture.height
            top = picture.top

            # 删除指定位置的图片
            if (top < 10 and height < 30):
                picture.delete()
    wb.save('./data/' + fileItem)

    # 关闭工作薄
    wb.close()

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
    # 新建工作薄（只打开不新建）
    app = xw.App(visible=True, add_book=False)
    # wb = app.books.add()

    originPath = './origin'
    fileList = getFileList(originPath)
    print(fileList)
    # 运行之前先清空data
    # if os.path.exists('./data'):
    #     os.removedirs("./data")
    # 创建data文件夹
    mkdir('./data')
    for fileItem in fileList:
        editExlXL(app, originPath, fileItem)
    # 退出excel
    app.quit()
editAll()