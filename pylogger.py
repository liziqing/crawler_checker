# -*- coding: utf-8 -*-
import logging
# from beaker.container import logger
class Pylogger:
    def init_log(self):   
        # 创建一个logger 
        logger = logging.getLogger('checker_logger') 
        logger.setLevel(logging.ERROR) 
           
        # 创建一个handler，用于写入日志文件 
        fh = logging.FileHandler('./log/checker1.log') 
        fh.setLevel(logging.ERROR) 
           
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