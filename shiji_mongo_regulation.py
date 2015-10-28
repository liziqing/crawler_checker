# -*- coding: utf-8 -*-
class MongoRegulation:
    #baseItem
    def item_checker(self, data, logger):
        #gender list
        gender_list = ['baby', 'toddler', 'girls', 'boys', 'women', 'men', 'unisex', 'kid-unisex']
        #product id
        try:
            item_id = data['show_product_id']
        except:
            logger.error("show_product_id is KeyError")
        data = dict(data)
        self.pyassert('goods', item_id, 'url', data, unicode, logger)    
        self.pyassert('goods', item_id, 'title', data, unicode, logger)
        try:
			if type(float(data['list_price'])) == float:
				pass
        except ValueError, e:
            logger.error(self.item_error_msg('goods', item_id, 'list_price num'))
        try:
            if type(float(data['current_price'])) == float:
                pass
        except ValueError, e:
            logger.error(self.item_error_msg('goods', item_id, 'current_price num'))
        try:
            if float(data['list_price'])<float(data['current_price']):
                logger.error(self.item_error_msg('goods', item_id, 'current_price > list_price'))
        except ValueError, e:
                logger.error(self.item_error_msg('goods', item_id, 'current_price or list_price num'))
        self.pyassert('goods', item_id, 'desc', data, unicode, logger)
        self.pyassert('goods', item_id, 'color', data, list, logger)
        if len(data['color']) != len(set(data['color'])):
            logger.error(self.item_error_msg('goods', item_id, 'colors item'))
        self.pyassert('goods', item_id, 'size', data, list, logger)
        if len(data['size']) != len(set(data['size'])):
            logger.error(self.item_error_msg('goods', item_id, 'sizes item'))
        self.pyassert('goods', item_id, 'dimensions', data, list, logger)
        if len(data['dimensions']) != len(set(data['dimensions'])):
            logger.error(self.item_error_msg('goods', item_id, 'dimensions item'))
        self.pyassert('goods', item_id, 'brand', data, unicode, logger)
        self.pyassert('goods', item_id, 'from_site', data, unicode, logger)
        self.pyassert('goods', item_id, 'product_type', data, unicode, logger)
        self.pyassert('goods', item_id, 'category', data, unicode, logger)
        self.pyassert('goods', item_id, 'cover', data, unicode, logger)
        if data['gender'] not in gender_list:
            logger.error(self.item_error_msg('goods', item_id, 'gender'))
                         
    #colorItem
    def color_checker(self, data, logger):
        try:
            item_id = data['show_product_id']
        except:
            logger.error("show_product_id is KeyError")
      
        self.pyassert('goods_colors', item_id, 'from_site', data, unicode, logger)
        self.pyassert('goods_colors', item_id, 'name', data, unicode, logger)
        self.pyassert('goods_colors', item_id, 'cover', data, unicode, logger)
        self.pyassert('goods_colors', item_id, 'images', data, list, logger)
        
    #skuItem
    def sku_checker(self, data, logger):
        try:
            item_id = data['show_product_id']
        except:
            logger.error("show_product_id is KeyError")
        self.pyassert('skus', item_id, 'from_site', data, unicode, logger)
        self.pyassert('skus', item_id, 'id', data, unicode, logger)
        if float(data['list_price'])<float(data['current_price']):
            logger.error(self.item_error_msg('skus', item_id, 'current_price or list_price'))
        try:
            if not type(float(data['list_price'])):
				pass
        except ValueError,e:
            logger.error(self.item_error_msg('skus', item_id, 'list_price num'))
        try:
			if not type(float(data['current_price'])):
				pass
        except ValueError, e:
            logger.error(self.item_error_msg('skus', item_id, 'current_price num'))
        self.pyassert('skus', item_id, 'is_outof_stock', data, bool, logger)
        self.pyassert('skus', item_id, 'color', data, unicode, logger)
        self.pyassert('skus', item_id, 'size', data, unicode, logger)
        
    def item_error_msg(self, collection, item_id, column_type):
        return item_id+": "+collection+" --"+column_type+"-- is not correct"
    
    def pyassert(self, collection, item_id, item_type, data, target_type, logger):       
        try:
            if not type(data[item_type]) == target_type:
                logger.error(self.item_error_msg(collection, item_id, item_type))
        except KeyError, e:
            logger.error(item_type+"is KeyError")

    def print_msg(self, msg):
        print msg

        
        

