# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CortexItem(scrapy.Item):
    dates = scrapy.Field()
    comments = scrapy.Field()
    identities = scrapy.Field()
    source = scrapy.Field()
    
    
