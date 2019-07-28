__author__ = 'Administrator'
# coding=utf-8
import os
import time,datetime
import xlwt,xlrd
from Util import logutil


# 创建excel
def createExcel(filename):  # 定义函数，文件名称包含路径
    wbk = xlwt.Workbook()  # excel对象
    sheet = wbk.add_sheet('sheet1')  # 创建sheet表
    wbk.save(filename)  # 保存文件路径+名称


# 删除excel
def delExcel(filename):
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d')
    if os.path.exists(filename):
        os.remove(filename)
        logutil.writeLog(
            "E:\PycharmProjects\test\lihonghua\work\logs" + nowtime + ".log" , "info", "程序将文件删除")
    else:
        logutil.writeLog(
            "E:\PycharmProjects\test\lihonghua\work\logs" + nowtime + ".log" , "info" , "程序未找到")


