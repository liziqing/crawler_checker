# -*- coding: utf-8 -*-
import logging
import sys
import os
from datetime import datetime
# from beaker.container import logger
class Pylogger:
    def init_log(self):   
        # 创建一个logger 
        logger = logging.getLogger('checker_logger') 
        logger.setLevel(logging.ERROR) 
        
        log_dir='/var/log/crawler_checker'
        now = datetime.now().strftime("%m%d%H%M%S")
        if os.path.exists(log_dir):
            log_dir = log_dir+'/'+str(now)+".log"
            # 创建一个handler，用于写入日志文件 
            fh = logging.FileHandler(log_dir) 
            fh.setLevel(logging.ERROR) 
        else:
            print 'log_dir Error! please make dir path: /var/log/crawler_checker!'
            sys.exit(1)
           
    #     # 再创建一个handler，用于输出到控制台 
    #     ch = logging.StreamHandler() 
    #     ch.setLevel(logging.DEBUG) 
           
        # 定义handler的输出格式 
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
        fh.setFormatter(formatter) 
    #     ch.setFormatter(formatter) 
        
        # 给logger添加handler 
        logger.addHandler(fh) 
    #     logger.addHandler(ch) 
           
        # 记录一条日志 
    #     logger.info('foorbar') 
        return logger