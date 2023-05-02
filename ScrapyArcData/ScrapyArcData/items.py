# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyarcdataTableItem(scrapy.Item):
    table_name = scrapy.Field()
    table_data = scrapy.Field()

class ScrapyarcdataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    brand = scrapy.Field()
    url = scrapy.Field()
    hostname = scrapy.Field()
    robot = scrapy.Field()
    tables = scrapy.Field()

