from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError, TCPTimedOutError

import scrapy
import logging
import json

import os
import datetime
from ScrapyArcData.items import ScrapyarcdataTableItem, ScrapyarcdataItem
from Utils import constants


# scrapy genspider spider_ArcData_Tables http://192.168.115.50/FRS/awdata.stm
logger = logging.getLogger(__name__)


# class SpiderArcdataTablesSpider(scrapy.Spider):
#     name = "spider_ArcData_Tables"
class froniusSpider(scrapy.Spider):
    name = "froniusSpider"
    countIp = 0
    
    # allowed_domains = ["192.168.115.50"]
    start_urls = [
        "http://192.168.115.42/FRS/awdata.stm",
        "http://192.168.115.43/FRS/awdata.stm",
        "http://192.168.115.44/FRS/awdata.stm",
        "http://192.168.91.14/FRS/awdata.stm",
        "http://192.168.91.15/FRS/awdata.stm",
        "http://192.168.91.16/FRS/awdata.stm",
        "http://192.168.91.17/FRS/awdata.stm",
        "http://192.168.91.18/FRS/awdata.stm",
        "http://192.168.91.20/FRS/awdata.stm",
        "http://192.168.91.21/FRS/awdata.stm",
        "http://192.168.91.23/FRS/awdata.stm",
        "http://192.168.91.24/FRS/awdata.stm",
        "http://192.168.91.26/FRS/awdata.stm",
        "http://192.168.91.27/FRS/awdata.stm",
        "http://192.168.91.28/FRS/awdata.stm",
        "http://192.168.31.13/FRS/awdata.stm",
        "http://192.168.31.14/FRS/awdata.stm",

        # "http://169.254.5.135/FRS/awdata.stm",
        # "http://169.254.4.174/FRS/awdata.stm",
        # "http://192.168.91.71/FRS/awdata.stm",
        # "http://192.168.91.72/FRS/awdata.stm",
        # "http://192.168.91.73/FRS/awdata.stm",
        # "http://192.168.91.74/FRS/awdata.stm",
        # "http://192.168.91.75/FRS/awdata.stm",
        # "http://192.168.91.76/FRS/awdata.stm",
        # "http://192.168.91.77/FRS/awdata.stm",
        # "http://192.168.91.78/FRS/awdata.stm",
        # "http://192.168.91.79/FRS/awdata.stm",
        # "http://192.168.91.80/FRS/awdata.stm",
        # "http://192.168.91.81/FRS/awdata.stm",
        # "http://192.168.31.21/FRS/awdata.stm",
        # "http://192.168.31.22/FRS/awdata.stm",
    ]

    # start_urls = ['http://192.168.115.42/FRS/awdata.stm','http://192.168.91.14/FRS/awdata.stm']
    
#linlon y fronius


    ipRobotDict = {}

    def __init__(self, url=None, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [url] if url else self.start_urls

    def start_requests(self):
        # len(self.start_urls)
        counter=1
        for url in self.start_urls:
            if url not in self.ipRobotDict:
                self.ipRobotDict[url] = counter
            counter += 1

        for url in self.start_urls:
            logger.info('start request with url {0}'.format(url))
            yield scrapy.Request(url=url, callback=self.parse, errback=self.handle_error)

    def parse(self, response):
        try:
            self.countIp += 1
            self.url = response.url
            logger.info('Starting {0} ({1}/{2})'.format(self.url,self.countIp,len(self.start_urls)))
            
            arcDataHeader = response.css('body > table:nth-child(1) > tr > td > table > tr > td:nth-child(2) > strong > font:nth-of-type(2)::text')
            arcDataHostName = arcDataHeader[0].re_first(r''+constants.HOSTNAME+'\s*(.*)')
            self.arcDataHostName = 'Hostname_None' if arcDataHostName is None else arcDataHostName.strip()

            arcDataRobotNo = arcDataHeader[1].re_first(r''+constants.ROBOT_NO+'\s*(.*)')
            self.arcDataRobotNo = 'Robot_None' if arcDataRobotNo is None else arcDataRobotNo.strip()


            Weld_Procedure_Data = response.css('a[name="Weld_Procedure_Data"] ~ table')[0]
            referencesWP = self.get_weld_procedure_data(Weld_Procedure_Data)
            if referencesWP is None: 
                return

            
            data_ArcData = ScrapyarcdataItem()
            data_ArcData['id'] = self.ipRobotDict.get(self.url) if self.url in self.ipRobotDict else 9999 #self.countIp
            data_ArcData['brand'] = constants.FRONIUS
            data_ArcData['url'] = self.url
            data_ArcData['hostname'] = self.arcDataHostName
            data_ArcData['robot'] = self.arcDataRobotNo
            data_ArcData['tables'] = self.get_tables_weld_schedule_data(response, referencesWP)
            
            logger.info('Finish {0} ({1}/{2})'.format(self.url,self.countIp,len(self.start_urls)))
            yield data_ArcData

        except Exception as err:
            logger.error('Error: {0}'.format(err))
    

    def handle_error(self, failure):
        msg = ''
        if failure.check(HttpError):
            # error HTTP, como 404 o 500
            response = failure.value.response
            msg = "HTTP Error {0} in URL {1}:\n{2}".format(response.status, response.url, response.text.replace("\r\n", ""))
            logger.error(msg)
        elif failure.check(DNSLookupError):
            # error de resolución de DNS
            request = failure.request
            msg = "DNS error in URL {0}:\n{1}".format(request.url, str(failure))
            logger.error(msg)
        elif failure.check(TimeoutError, TCPTimedOutError):
            # error de tiempo de espera
            request = failure.request
            msg = "Timeout error in URL {0}:\n{1}".format(request.url, str(failure))
            logger.error(msg)
        else:
            # otros errores
            request = failure.request
            msg = "Error in URL {0}:\n{1}".format(request.url, str(failure))
            logger.error(msg)
    
        file_name = f"Errors_ArcData_{datetime.datetime.now().strftime('%Y-%m-%d')}_{constants.FRONIUS}.txt"

        if os.path.exists(file_name):
            with open(self.file_name, "a") as f:
                f.write(f"\n\n{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -> {msg}")
        else:
            with open(file_name, "w") as f:
                f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -> {msg}")

    def get_weld_procedure(self, table):
        try:
            wsd_headers = [str(header.css('b::text').get().strip()).lower() for header in table.css('tr')[0].css('td')]
            exist_in_constants, unfilled_constants, no_exist_in_constants = constants.FroniusWeldScheduleData.is_valid_value(wsd_headers)

            if not exist_in_constants:
                logger.warning('IP:{0} HostName:{1} Robot:{2} Msg:{3} {4}'.format(self.url,self.arcDataHostName,self.arcDataRobotNo,"The Weld Procedure Data contains columns that are not registered in the system. Please add the new columns to the system constants to avoid errors.",no_exist_in_constants))
                return None
                
            wsd = []
            for row in table.css('tr')[1:]:
                values = [value.css('td::text').get().strip() if value.css('td::text').get() else '' for value in row.css('td:not(:last-child)')]
                last_value = row.css('td:last-child div::text').get().strip() if row.css('td:last-child div::text').get() else ''
                values.append(last_value)

                wsd_tmp = dict(zip(wsd_headers, values)) # convert to dictionary the information
                wsd_tmp.update({key: constants.NA for key in unfilled_constants}) # Add columns to the dictionary that are filled with default values
                wsd.append(wsd_tmp)

            return wsd
        
        except Exception as err:
            logger.error('Error: {0}'.format(err))
            return None
        
    def get_weld_procedure_data(self, table):
        try:
            wpd_headers = [ str(header.css('b::text').get().strip()).lower() for header in table.css('tr:first-child td')]
            wpd = []
            exist_in_constants, unfilled_constants , no_exist_in_constants =  constants.WeldProcedureData.is_valid_value(wpd_headers)

            if not exist_in_constants:
                logger.warning('IP:{0} HostName:{1} Robot:{2} Msg:{3} {4}'.format(self.url,self.arcDataHostName,self.arcDataRobotNo, "The Weld Procedure Data contains columns that are not registered in the system. Please add the new columns to the system constants to avoid errors.",no_exist_in_constants))
                return None
            
            for row in table.css('tr')[1:]:
                row_values = []
                for i, col in enumerate(row.css('td')):
                    if i is not 1:
                       row_values.append(col.css('td::text').get().strip() if col.css('td::text').get()  else '')
                    else:
                        if col.css('td a::attr(href)').get() is None:
                            row_values.append('Sch_None')
                            logger.warning('IP:{0} HostName:{1} Robot:{2} Msg:{3} (Num:{4})'.format(self.url,self.arcDataHostName,self.arcDataRobotNo,"The Weld Procedure Data has not references to Sch",row_values[0]))
                        else:
                            row_values.append(col.css('td a::attr(href)').get().strip().replace('#', ''))

                wpd_tmp = dict(zip(wpd_headers, row_values)) # convert to dictionary the information
                wpd_tmp.update({key: constants.NA for key in unfilled_constants}) # Add columns to the dictionary that are filled with default values
                wpd.append(wpd_tmp)

            return wpd
        
        except Exception as err:
            logger.error('Error: {0}'.format(err))
            return None

            
    def get_tables_weld_schedule_data(self, response, listSchedules):
        try:
            logger.info('Mapping Table Content from {0}'.format(self.url))
            list_wsd = []

            for sch in listSchedules:
                
                tableRef = response.css(f'a[name="{sch[constants.WeldProcedureData.SCH.value.lower()]}"] ~ table')
                tableRef = tableRef[0] if len(tableRef) else None
                if tableRef is not None:
                    list_wsd.append(ScrapyarcdataTableItem(table_name=f"WSD_{self.arcDataHostName}_{sch[constants.WeldProcedureData.SCH.value.lower()]}", table_data=self.get_weld_procedure(tableRef)))

            return list_wsd
        
        except Exception as err:
            logger.error('Error: {0}'.format(err))
            return None