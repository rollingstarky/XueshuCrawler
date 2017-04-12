# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import json
import pymysql
import pymongo

#写入Json文件
class XueshuPipeline(object):

	def __init__(self):
		self.file=open('items.json','w')
	def process_item(self, item, spider):
		line=json.dumps(dict(item),ensure_ascii=False) +"\n"
		self.file.write(line)
		return item
	def spider_closed(self,spider):
		self.file.close()

#写入Mysql数据库
class MysqlPipeline(object):
	def __init__(self):
		#连接本地数据库
		self.conn=pymysql.connect(host=settings['MYSQL_HOST'],user=settings['MYSQL_USER'],password=settings['MYSQL_PASS'],db=settings['MYSQL_DB'],charset='utf8')
		self.cursor=self.conn.cursor()
		self.cursor.execute("truncate table xueshu;")
		self.conn.commit()

	def process_item(self,item,spider):
		data=dict(item)
		for key in data:
			if key=='title':
				data[key]=''.join(data[key])
			else:
				data[key]=' '.join(data[key])
		self.cursor.execute("insert into scholar.xueshu (title,author,publish,year,cite,subject,abstract) values (%s,%s,%s,%s,%s,%s,%s)",(data['title'],data['author'],data['publish'],data['year'],data['cite'],data['subject'],data['abstract']))
		self.conn.commit()

	def spider_closed(self,spider):
		self.cursor.close()
		self.conn.close()

class MongoPipeline(object):
	def __init__(self):
		self.mongo_uri=settings['MONGO_URI']
		self.mongo_db=settings['MONGO_DB']
		self.collection=settings['MONGO_COLLECTION']		
	
#	@classmethod
#	def from_crawler(cls,crawler):
#		return cls(
#			mongo_uri=crawler.settings.get('MONGO_URI'),
#
#			mongo_db=crawler.settings.get('MONGO_DATABASE')
	
	def open_spider(self,spider):
		self.client=pymongo.MongoClient(self.mongo_uri)
		self.db=self.client[self.mongo_db]

	def close_spider(self,spider):
		self.client.close()

	def process_item(self,item,spider):
		for key in item:
			if key=='title':
				item[key]=''.join(item[key])
		self.db[self.collection].insert(dict(item))
		return item
		
	

