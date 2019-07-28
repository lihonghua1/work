__author__ = 'Administrator'
# coding=utf8
import logging


def writeLog(filname,logType,logInfo):
    logging.basicConfig(
        level=logging.debug,  # 定义输出到文件的log级别，大于此级别的都被输出
        format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',  # 定义输出log的格式
        datefmt='%Y-%m-%d %A %H:%M:%S',  # 时间
        filemode='w')  # 写入模式“w”或“a”
    console = logging.StreamHandler()  # 定义console handler
    console.setLevel(logging.INFO)  # 定义该handler级别
    formatter = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')  # 定义该handler格式
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)  # 实例化添加handler
    if logType == "info":
        logging.info(logInfo)
    elif logType == "error":
        logging.error(logInfo)
    elif logType == "debug":
        logging.debug(logInfo)
