import scrapy
import logging
import json

import os
import datetime

# scrapy genspider spider_ArcData_Tables http://192.168.115.50/FRS/awdata.stm
logging.basicConfig(filename='app.log', level=logging.DEBUG)

logger = logging.getLogger(__name__)

class SpiderArcdataTablesSpider(scrapy.Spider):
    name = "spider_ArcData_Tables"
    file_created = False
    file_name = ""
    # allowed_domains = ["192.168.115.50"]
  
    start_urls = [
    "http://192.168.115.30/FRS/awdata.stm",
    "http://192.168.115.53/FRS/awdata.stm"
    "http://192.168.83.170/FRS/awdata.stm",
    "http://192.168.83.171/FRS/awdata.stm"
    ]

    def parse(self, response):
        try:
            # print('Getting Content...')
            # logger.setLevel(logging.DEBUG)
            logger.info('Getting Content...')

            tables = {}
            table1 = response.css('a[name="AWE1WP01"] ~ table')[0]
            table2 = response.css('a[name="AWE1WP02"] ~ table')[0]

            tables["Weld_Schedule_Data_AWE1WP01"] = table1
            tables["Weld_Schedule_Data_AWE1WP02"] = table2

            data_objects = {}
            for key, value in tables.items():
                dataObj = self.convert_table_to_object(value)
                if dataObj:
                    data_objects[key] = dataObj

            # print(data_objects)
            logger.info(data_objects)

            if not self.file_created:
                self.file_name = "data_objects_" + datetime.datetime.now().strftime("%Y-%m-%d") + ".json"

                if os.path.isfile(self.file_name):
                    # If the file already exists, add a number to the end of the file name.
                    i = 1
                    while True:
                        new_filename = f"data_objects_{datetime.datetime.now().strftime('%Y-%m-%d')}({i}).json"
                        if not os.path.isfile(new_filename):
                            self.file_name = new_filename
                            break
                        i += 1
                self.file_created = True

            # Save data_objects to a JSON file
            with open(self.file_name, 'a') as json_file:
                json.dump(data_objects, json_file)
                
            logger.info("End process")

        except Exception as err:
            # print('Error:', err)
            logger.error('Error:', err)

    def convert_table_to_object(self, table):
        try:
            default_headers = ['Num', 'WFS', 'Trim', 'UltimArc', 'Weld Speed', 'Time', 'Comment']
            headers = [header.css('b::text').get().strip() for header in table.css('tr')[0].css('td')]
            if len(headers) < len(default_headers):
                headers = default_headers
                
            data = []
            for row in table.css('tr')[1:]:
                values = [value.css('td::text').get().strip() if value.css('td::text').get() else '' for value in row.css('td:not(:last-child)')]
                last_value = row.css('td:last-child div::text').get().strip() if row.css('td:last-child div::text').get() else ''
                values.append(last_value)
                data.append(dict(zip(headers, values)))
            return data
        except Exception as err:
            # print('Error:', err)
            logger.error('Error:', err)
            return None
