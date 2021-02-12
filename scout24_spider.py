from scrapy import Spider, Request
from scout24.items import Scout24Item
import re
import math

class Scout24Spider(Spider):
    name = "scout24_spider"
    allowed_urls = ['https://scout24.ch/de/']
    start_urls = ['https://www.autoscout24.ch/de/autos/alle-marken?sort=makemodel_asc&page=1&vehtyp=10']

    def parse(self, response):
        num_pages = int(response.xpath('//button[@class="page-link"]/text()').extract()[-1]) #currently wrong 
        result_urls = [f'https://www.autoscout24.ch/de/autos/alle-marken?page={i+1}&vehtyp=10' for i in range(num_pages)] #range(num_pages)
        # num_items = 20 #['https://www.autoscout24.ch/de/autos/alle-marken?page=1&vehtyp={j}' ]

        for url in result_urls:#[:5]
            yield Request(url=url, callback=self.parse_results_page)
        
    def parse_results_page(self, response):

        rows =  response.xpath('//article[@class="vehicle-card card mb-5 mb-sm-6"]') #response.xpath('//div[@class="row no-gutters vehicle-info with-insurance-link"]')

        for row in rows:

            model = row.xpath('.//div[@class="d-flex mr-auto font-weight-bold text"]/text()').extract_first()
            price = row.xpath('.//span[@class="d-inline-block font-weight-bold h2 mr-2 mb-0"]/text()').extract_first()
            data, km = row.xpath('.//span[@class="vehicle-tech-spec"]/text()').extract()

            item = Scout24Item()
            item['model'] = model
            item['price'] = price
            item['data'] = data
            item['km'] = km

            yield item
    #         product_url = row.xpath('.//a[@class="base-nav-link stretched-link"]/@href').extract_first()
    #         product_url = 'https://www.autoscout24.ch' + product_url

    #         meta = {'model': model, 
    #                'price': price,
    #                'data': data,
    #                'km': km}

    #         yield Request(url=product_url, callback=self.parse_product_page, meta=meta)

    # def parse_product_page(self, response):
    #     print(response.meta)


    #     meta = {'model': model, 
    #             'price': price,
    #             'data': data,
    #             'km': km}

    #     for url in result_urls:
    #         yield Request(url=url, callback=self.parse_result_page, meta=meta)

    # def parse_result_page(self, response):
    #     product_urls = response.xpath('//a[@class="base-nav-link stretched-link"]/@href').extract()
    #     product_urls = ['https://www.autoscout24.ch' + url for url in product_urls][1]

    #     ps = product_urls.xpath('//span[class="raw-html key-value-value text-ellipsis"]/text/()').extract_first()
    #     elektro = product_urls.xpath('//span[@class="raw-html key-value-value text-ellipsis"]/text()').extract_first()









