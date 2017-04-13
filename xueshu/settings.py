# -*- coding: utf-8 -*-

# Scrapy settings for xueshu project

BOT_NAME = 'xueshu'

SPIDER_MODULES = ['xueshu.spiders']
NEWSPIDER_MODULE = 'xueshu.spiders'

#设置不遵守robots.txt协议
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',

#设置请求头（防止被服务器屏蔽）
DEFAULT_REQUEST_HEADERS = {
    'accept': 'image/webp,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.8',
    'referer': 'http://xueshu.baidu.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
}
#}

# Enable or disable spider middlewares
#SPIDER_MIDDLEWARES = {
#    'xueshu.middlewares.XueshuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
#DOWNLOADER_MIDDLEWARES = {
#    'xueshu.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}


#启用自定义的pipeline
#如果想启用Json文件和Mysql数据库，请移除指定行的注释（60行，61行）
ITEM_PIPELINES = {
    'xueshu.pipelines.XueshuPipeline': 300,
    'xueshu.pipelines.MysqlPipeline':500,
    'xueshu.pipelines.MongoPipeline':800,
}

ALL_PAGE=2
PHANTOM_PATH='E:\\software\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'
KEY_WORD='非织造'
#mysql连接参数设置
MYSQL_HOST='localhost'
MYSQL_USER='scholar'
MYSQL_PASS='starky'
MYSQL_DB='scholar'

#Mongodb连接参数
MONGO_URI='localhost:27017'
MONGO_DB='baidu'
MONGO_COLLECTION='xueshu'
# Enable and configure the AutoThrottle extension (disabled by default)
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

