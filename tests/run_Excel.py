__author__ = 'Administrator'
# coding=utf-8
import os
import time
import datetime
import xlwt
from Util import logutil, Excelutil
start = time.time()
excelPath = "E:/PycharmProjects/test/lihonghua/work/ExcelFile/"
nowtime = datetime.datetime.now().strftime('%Y-%m-%d')
filename = excelPath + nowtime + ".xls"
Excelutil.createExcel(filename)
wbk = xlwt.Workbook()
sheet1 = wbk.add_sheet("自动化1")
style = xlwt.XFStyle()  # 格式信息
font = xlwt.Font()  # 字体基本设置
font.bold = True  # 字体加粗
font.height = 220  # 字体大小，
style.font = font
sheet1.write(0, 0, "账号", style)  # 设置账号字体加粗
sheet1.write(0, 1, "密码", style)  # 设置密码字体加粗

# 生成数据
user_ids = []  ##定义一个空列表
for i in range(1, 1001):  ##生成1到1000的数
    s = '8451252630%0.3d' % i  ##设定前几位为'8451252630，后三位001的模式递增
    user_ids.append(s)  ##在定义的空列表中添加元素
user_dict = {}.fromkeys(user_ids, 'Faxuan.%1234')  ##生成字典，方式位不同的key对应相同的value数值，用到了fromkeys
i = 1
for k in user_dict:  ##编历字典，将账号插入账号列，密码插入密码列
    sheet1.write(i, 0, int(k))
    sheet1.write(i, 1, user_dict[k])
    i += 1
sheet2 = wbk.add_sheet('自动化2')
sheet2.write(0, 0, "平均值", style)
sheet2.write(0, 1, "=AVERAGE(自动化1!A1:A" + str(i) + ")")
nowtime = datetime.datetime.now().strftime("%Y-%m-%d")
wbk.save(filename)

fileDirInfo = list(os.walk(excelPath))  # 获得文件夹下所有文件目录信息，有一个元素的LIST
fileDirInfoList = fileDirInfo[0]  # 取出第一个数据类型为元组的数值 ，元组中有3个元素，分别为：当前目录，所有子文件夹的LIST,所有子文件的LIST
curFilePath = fileDirInfoList[0]  # 当前目录
allFileList = fileDirInfoList[2]  # 含所有子文件的LIST
os.chdir(curFilePath)
for f in allFileList:  # 遍历含子文件的LIST
    fileCreateTime = time.strftime('%Y-%m-%d', time.localtime(os.path.getmtime(f)))  # 取文件创建时间并格式化
    if fileCreateTime < nowtime:
        Excelutil.delExcel(curFilePath + f)  # 如果文件创建时间小于当前日期，调用删除文件函数
end = time.time()
print (end-start)
