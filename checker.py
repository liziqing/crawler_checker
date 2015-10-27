# -*- coding: utf-8 -*-
from pymongo import MongoClient
from shiji_mongo_regulation import MongoRegulation
from pylogger import Pylogger
connection = MongoClient('127.0.0.1', 27017)
db = connection.shiji_shop
goods = db.goods
colors = db.goods_colors
skus = db.skus

logger = Pylogger().init_log()
mongoRegulation = MongoRegulation()
for good in goods.find():
    mongoRegulation.item_checker(good, logger)
 
for color in colors.find():
    mongoRegulation.color_checker(color, logger)
 
for sku in skus.find():
    mongoRegulation.sku_checker(sku, logger)
    
