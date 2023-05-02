# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging
from itemadapter import ItemAdapter
import json
import datetime
import os
from itemadapter import ItemAdapter

logger = logging.getLogger(__name__)

class ScrapyarcdataPipeline:
    def process_item(self, item, spider):
        return item

class JsonWriterPipeline:

    def __init__(self):
        self.files = {}
        self.items = {}

    def open_spider(self, spider):
        file_name = f"ArcData_{datetime.datetime.now().strftime('%Y-%m-%d')}_{spider.name}.json"
        if os.path.isfile(file_name):
            i = 1
            while True:
                new_filename = f"ArcData_{datetime.datetime.now().strftime('%Y-%m-%d')}_{spider.name}({i}).json"
                if not os.path.isfile(new_filename):
                    file_name = new_filename
                    break
                i += 1
        self.files[spider.name] = file_name
        self.items[spider.name] = []

    def close_spider(self, spider):
        if len(self.items[spider.name]) == 0:
            logger.warning("Entered to close spider method, but did not save any information for {0}".format(spider.name))
        else:
            with open(self.files[spider.name], 'w') as f:
                sorted_items = sorted(self.items[spider.name], key=lambda x: x['id'])
                json.dump(sorted_items, f)

    def process_item(self, item, spider):
        data = ItemAdapter(item).asdict()
        self.items[spider.name].append(data)
        return item