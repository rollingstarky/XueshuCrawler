import scrapy
from xueshu.items import XueshuItem
#import requests
#from bs4 import BeautifulSoup
#from scrapy.http import Request
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.conf import settings

class XueshuSpider(scrapy.Spider):
	name="xueshu"
	page=settings['ALL_PAGE']
#	key_word=settings['KEY_WORD']
	allowed_domains=["baidu.com"]

	start_urls=['http://xueshu.baidu.com/s?wd='+'非织造'+'&ie=utf-8&pn='+str(i)+'0' for i in range(page)]
	
##get_abstract的另外两个版本：
#	def get_abstract(self,url):
#		session = requests.Session()
#		req = session.get(url, headers=HEADERS)
#		bsObj = BeautifulSoup(req.text)
#		return bsObj.find("p",{"class":"abstract"}).get_text()

#	def get_abstract(self,url):
#		session = requests.Session()
#		req = session.get(url)
#		f=open('abstract.html','w')
#		f.writelines(req.text)
#		return Selector(text=req.text).xpath('//div[@class="abstract_wr"]/p[2]/text()').extract()[0]

	def get_abstract(self,link):
		#通过无头浏览器PhantomJS加载动态页面(即Javascript执行后的页面)
		driver=webdriver.PhantomJS(executable_path=settings['PHANTOM_PATH'])
		driver.get(link)

		#确保网页加载完毕
		try:
			element=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,"dtl_r")))
		finally:
			pageSource=driver.page_source
		return Selector(text=pageSource).xpath('//div[@class="abstract_wr"]/p[2]/text()').extract()[0]

	
	def parse(self,response):
#		filename = 'xueshu.html'
#		with open(filename, 'wb') as f:
#			f.write(response.body)
		for sel in response.xpath('//div[@srcid]'):
			item=XueshuItem()
			for  cell in sel.xpath('div[1]'):
				item['title']=cell.xpath('h3//a//text()').extract()
				item['link']=cell.xpath('h3/a/@href').extract()
				item['author']=cell.xpath('div[1]/span[1]//a/text()').extract()
				link='http://xueshu.baidu.com'+cell.xpath('h3/a/@href').extract()[0]
				item['publish']=cell.xpath('div[1]/span[2]/a/@title').extract()
				item['year']=cell.xpath('div[1]/span[3]/text()').extract()
				item['cite']=cell.xpath('div[1]/span[4]/a/text()').extract()
				item['abstract']=self.get_abstract(link)
#				self.log(self.get_abstract(link))
			item['subject']=sel.xpath('div[2]/div[1]//a/text()').extract()
			yield item






