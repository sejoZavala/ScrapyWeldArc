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
class lincolnSpider(scrapy.Spider):
    name = "lincolnSpider"
    countIp = 0

    # allowed_domains = ["192.168.115.50"]

    start_urlsaaaa = [
        "http://192.168.115.30/FRS/awdata.stm",
        "http://192.168.115.31/FRS/awdata.stm",
        "http://192.168.115.32/FRS/awdata.stm",
        "http://192.168.115.36/FRS/awdata.stm",
        "http://192.168.115.37/FRS/awdata.stm",
        "http://192.168.115.38/FRS/awdata.stm",
        "http://192.168.115.40/FRS/awdata.stm",
        "http://192.168.115.41/FRS/awdata.stm",
        "http://192.168.115.45/FRS/awdata.stm",
        "http://192.168.115.46/FRS/awdata.stm",
        "http://192.168.115.50/FRS/awdata.stm",
        "http://192.168.115.51/FRS/awdata.stm",
        "http://192.168.115.55/FRS/awdata.stm",
        "http://192.168.115.56/FRS/awdata.stm",
        "http://192.168.115.61/FRS/awdata.stm",
        "http://192.168.115.62/FRS/awdata.stm",

        "http://192.168.115.53/FRS/awdata.stm",
        "http://192.168.115.54/FRS/awdata.stm",

        "http://192.168.115.58/FRS/awdata.stm",
        "http://192.168.115.59/FRS/awdata.stm",
        "http://192.168.115.63/FRS/awdata.stm",
        "http://192.168.115.49/FRS/awdata.stm",
        "http://192.168.115.68/FRS/awdata.stm",
        "http://192.168.115.69/FRS/awdata.stm",
        "http://192.168.116.41/FRS/awdata.stm",
        "http://192.168.116.42/FRS/awdata.stm",
        "http://192.168.116.43/FRS/awdata.stm",
        "http://192.168.116.45/FRS/awdata.stm",
        "http://192.168.116.46/FRS/awdata.stm",
        "http://192.168.116.47/FRS/awdata.stm",
        "http://192.168.116.49/FRS/awdata.stm",
        "http://192.168.116.50/FRS/awdata.stm",
        "http://192.168.116.52/FRS/awdata.stm",
        "http://192.168.116.53/FRS/awdata.stm",
        "http://192.168.116.55/FRS/awdata.stm",

        "http://192.168.116.56/FRS/awdata.stm",
        "http://192.168.116.58/FRS/awdata.stm",
        "http://192.168.116.59/FRS/awdata.stm",

        "http://192.168.83.170/FRS/awdata.stm",
        "http://192.168.83.171/FRS/awdata.stm",
        "http://192.168.83.175/FRS/awdata.stm",
        "http://192.168.83.176/FRS/awdata.stm",
        "http://192.168.83.172/FRS/awdata.stm",
        "http://192.168.83.173/FRS/awdata.stm",
        "http://192.168.83.174/FRS/awdata.stm",

        "http://192.168.82.10/FRS/awdata.stm",
        "http://192.168.82.11/FRS/awdata.stm",
        "http://192.168.82.12/FRS/awdata.stm",
        "http://192.168.82.13/FRS/awdata.stm",
        "http://192.168.82.14/FRS/awdata.stm",
        "http://192.168.82.15/FRS/awdata.stm",
        "http://192.168.82.16/FRS/awdata.stm",
        "http://192.168.82.17/FRS/awdata.stm",
        "http://192.168.82.18/FRS/awdata.stm",
        "http://192.168.82.19/FRS/awdata.stm",
        "http://192.168.82.20/FRS/awdata.stm",
        "http://192.168.82.21/FRS/awdata.stm",
        "http://192.168.82.27/FRS/awdata.stm",
        "http://192.168.82.22/FRS/awdata.stm",
        "http://192.168.82.23/FRS/awdata.stm",
        "http://192.168.82.24/FRS/awdata.stm",
        "http://192.168.82.25/FRS/awdata.stm",
        "http://192.168.82.26/FRS/awdata.stm",
        "http://192.168.83.142/FRS/awdata.stm",
        "http://192.168.83.143/FRS/awdata.stm",
        "http://192.168.83.144/FRS/awdata.stm",
        "http://192.168.83.139/FRS/awdata.stm",
        "http://192.168.83.135/FRS/awdata.stm",
        "http://192.168.83.136/FRS/awdata.stm",
        "http://192.168.83.137/FRS/awdata.stm",
        "http://192.168.83.138/FRS/awdata.stm",
        "http://192.168.83.10/FRS/awdata.stm",
        "http://192.168.83.11/FRS/awdata.stm",

        "http://192.168.83.12/FRS/awdata.stm",
        "http://192.168.83.13/FRS/awdata.stm",
        "http://192.168.83.14/FRS/awdata.stm",
        "http://192.168.83.15/FRS/awdata.stm",
        "http://192.168.83.16/FRS/awdata.stm",
        "http://192.168.83.17/FRS/awdata.stm",
        "http://192.168.83.177/FRS/awdata.stm",
        "http://192.168.83.178/FRS/awdata.stm",
        "http://192.168.83.179/FRS/awdata.stm",
        "http://192.168.82.178/FRS/awdata.stm",
        "http://192.168.82.179/FRS/awdata.stm",
        "http://192.168.82.168/FRS/awdata.stm",
        "http://192.168.82.169/FRS/awdata.stm",
        "http://192.168.82.170/FRS/awdata.stm",
        "http://192.168.82.176/FRS/awdata.stm",
        "http://192.168.82.172/FRS/awdata.stm",
        "http://192.168.82.173/FRS/awdata.stm",
        "http://192.168.83.230/FRS/awdata.stm",
        "http://192.168.83.231/FRS/awdata.stm",
        "http://192.168.83.232/FRS/awdata.stm",
        "http://192.168.83.233/FRS/awdata.stm",
        "http://192.168.83.234/FRS/awdata.stm",
        "http://192.168.83.235/FRS/awdata.stm",
        "http://192.168.83.236/FRS/awdata.stm",
        "http://192.168.83.237/FRS/awdata.stm",
        "http://192.168.82.146/FRS/awdata.stm",
        "http://192.168.82.147/FRS/awdata.stm",
        "http://192.168.95.22/FRS/awdata.stm",
        "http://192.168.95.23/FRS/awdata.stm",
        "http://192.168.95.20/FRS/awdata.stm",
        "http://192.168.95.21/FRS/awdata.stm",
        "http://192.168.82.136/FRS/awdata.stm",
        "http://192.168.82.137/FRS/awdata.stm",
        "http://192.168.82.138/FRS/awdata.stm",
        "http://192.168.82.139/FRS/awdata.stm",
        "http://192.168.82.140/FRS/awdata.stm",
        "http://192.168.82.141/FRS/awdata.stm",

        "http://192.168.91.10/FRS/awdata.stm",
        "http://192.168.91.11/FRS/awdata.stm",
        "http://192.168.91.12/FRS/awdata.stm",
        "http://192.168.91.13/FRS/awdata.stm",


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



    # start_urls = ['http://192.168.116.58/FRS/awdata.stm','http://192.168.115.42/FRS/awdata.stm']
    start_urls = ['http://192.168.116.58/FRS/awdata.stm','http://192.168.116.56/FRS/awdata.stm']
    # start_urls = ['http://192.168.115.37/FRS/awdata.stm','http://192.168.83.234/FRS/awdata.stm']


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
            self.url = response.url
            logger.info('Starting {0}'.format(self.url))
            

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
            data_ArcData['brand'] = constants.LINCONL
            data_ArcData['url'] = self.url
            data_ArcData['hostname'] = self.arcDataHostName
            data_ArcData['robot'] = self.arcDataRobotNo
            data_ArcData['tables'] = self.get_tables_weld_schedule_data(response, referencesWP)

            logger.info('Finishing {0}'.format(self.url))
            yield data_ArcData

        except Exception as err:
            logger.error('Error in {0} Msg: {1}'.format(self.url, err))


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

        file_name = f"Errors_ArcData_{datetime.datetime.now().strftime('%Y-%m-%d')}_{constants.LINCONL}.txt"

        if os.path.exists(file_name):
            with open(file_name, "a") as f:
                f.write(f"\n\n{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -> {msg}")
        else:
            with open(file_name, "w") as f:
                f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -> {msg}")

    def get_weld_procedure(self, table):
        try:
            wsd_headers = [str(header.css('b::text').get().strip()).lower() for header in table.css('tr')[0].css('td')]
            exist_in_constants, unfilled_constants, no_exist_in_constants = constants.LincolnWeldScheduleData.is_valid_value(wsd_headers)

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
            logger.error('Error in {0} Msg: {1}'.format(self.url, err))
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
            logger.error('Error in {0} Msg: {1}'.format(self.url, err))
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
            logger.error('Error in {0} Msg: {1}'.format(self.url, err))
            return None