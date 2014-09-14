# -*- coding: utf-8 -*-

# Scrapy settings for ispider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ispider'

SPIDER_MODULES = ['ispider.spiders']
NEWSPIDER_MODULE = 'ispider.spiders'


#默认是深度优先，设置为广度优先
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ispider (+http://www.yourdomain.com)'
