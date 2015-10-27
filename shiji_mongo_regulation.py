# -*- coding: utf-8 -*-
class MongoRegulation:
    #baseItem
    def item_checker(self, data, logger):
        #gender list
        gender_list = ['baby', 'toddler', 'girls', 'boys', 'women', 'men', 'unisex', 'kid-unisex']
        #product id
        item_id = data['show_product_id']
        data = dict(data)
        self.pyassert(item_id, 'url', data['url'], unicode, logger)    
        self.pyassert(item_id, 'title', data['title'], unicode, logger)
        try:
			if type(float(data['list_price'])) == float:
				pass
        except ValueError, e:
            logger.error(self.item_error_msg(item_id, 'list_price num'))
        try:
            if type(float(data['current_price'])) == float:
                pass
        except ValueError, e:
            logger.error(self.item_error_msg(item_id, 'current_price num'))
        try:
            if float(data['list_price'])<float(data['current_price']):
                logger.error(self.item_error_msg(item_id, 'current_price > list_price'))
        except ValueError, e:
                logger.error(self.item_error_msg(item_id, 'current_price or list_price num'))
        self.pyassert(item_id, 'desc', data['desc'], unicode, logger)
        self.pyassert(item_id, 'color', data['color'], list, logger)
        if len(data['color']) != len(set(data['color'])):
            logger.error(self.item_error_msg(item_id, 'colors item'))
        self.pyassert(item_id, 'size', data['size'], list, logger)
        if len(data['size']) != len(set(data['size'])):
            logger.error(self.item_error_msg(item_id, 'sizes item'))
        self.pyassert(item_id, 'dimensions', data['dimensions'], list, logger)
        if len(data['dimensions']) != len(set(data['dimensions'])):
            logger.error(self.item_error_msg(item_id, 'dimensions item'))
        self.pyassert(item_id, 'brand', data['brand'], unicode, logger)
        self.pyassert(item_id, 'from_site', data['from_site'], unicode, logger)
        self.pyassert(item_id, 'product_type', data['product_type'], unicode, logger)
        self.pyassert(item_id, 'category', data['category'], unicode, logger)
        if data['gender'] not in gender_list:
            logger.error(self.item_error_msg(item_id, 'gender'))
                         
    #colorItem
    def color_checker(self, data, logger):
        item_id = data['show_product_id']
      
        self.pyassert(item_id, 'from_site', data['from_site'], unicode, logger)
        self.pyassert(item_id, 'name', data['name'], unicode, logger)
        self.pyassert(item_id, 'cover', data['cover'], unicode, logger)
        self.pyassert(item_id, 'images', data['images'], list, logger)
        
    #skuItem
    def sku_checker(self, data, logger):
        item_id = data['show_product_id']
        self.pyassert(item_id, 'from_site', data['from_site'], unicode, logger)
        self.pyassert(item_id, 'id', data['id'], unicode, logger)
        if float(data['list_price'])<float(data['current_price']):
            logger.error(self.item_error_msg(item_id, 'current_price or list_price'))
        try:
            if not type(float(data['list_price'])):
				pass
        except ValueError,e:
            logger.error(self.item_error_msg(item_id, 'list_price num'))
        try:
			if not type(float(data['current_price'])):
				pass
        except ValueError, e:
            logger.error(self.item_error_msg(item_id, 'current_price num'))
        self.pyassert(item_id, 'is_outof_stock', data['is_outof_stock'], bool, logger)
        self.pyassert(item_id, 'color', data['color'], unicode, logger)
        self.pyassert(item_id, 'size', data['size'], unicode, logger)
        
    def item_error_msg(self, item_id, column_type):
        return item_id+":  baseItem --"+column_type+"-- is not correct"
    
    def pyassert(self, item_id, item_type, data, target_type, logger):
        if not type(data) == target_type:
            logger.error(self.item_error_msg(item_id, item_type))
