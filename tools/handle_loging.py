# -*- coding: utf-8 -*-
# @Time    : 15/5/2021 下午 9:48
# @Author  : 海励
# @File    : handle_loging.py

import logging
from logging import handlers

from tools.handle_path import log_dir


#用函数封装
def handle_log():
    #创建日志收集器
    py_39 = logging.getLogger(name='py39')
    #创建日志收集渠道
    pycharm = logging.StreamHandler()#控制台渠道
    file = handlers.TimedRotatingFileHandler( filename=log_dir, when='D', encoding='utf-8',interval=1, backupCount=5)

    #日志格式
    fmt = '%(asctime)s-%(name)s-%(levelname)s-%(filename)s-%(funcName)s-[line:%(lineno)d]：%(message)s'
    log_fmt = logging.Formatter(fmt=fmt)

    #日志级别：收集器、渠道,可以不同的渠道输出日志级别不一样
    py_39.setLevel(logging.DEBUG)

    #给渠道添加日志格式
    pycharm.setFormatter(fmt=log_fmt)
    file.setFormatter(fmt=log_fmt)

    #渠道
    py_39.addHandler(pycharm)
    py_39.addHandler(file)
    return py_39

my_logger = handle_log()


#my_logger.info('test2021')


