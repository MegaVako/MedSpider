import scrapy
from scrapy.selector import HtmlXPathSelector
from medSpiderDemo.items import MedspiderdemoItem

class InterSpider(scrapy.Spider):
    name = 'xcSpider_v1.0'
    start_urls = ['https://flights.ctrip.com/international/search/round-ord0-hkg0?depdate=2019-12-21_2020-01-11&cabin=y_s&adult=1&child=0&infant=0']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 2}
                }
            })

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        count = 0
        self.logger.info(response)
        # temp = MedspiderdemoItem()
        # temp["tag"] = response.text
        # yield temp
        rootPath = '//div[contains(@class, "flight-list")]/span/div'

        namePath = './/div[contains(@class, "flight-airline")]/div[2]/div/span/text()'
        # linkPath = './/a[contains(@class,"a-link-normal a-text-normal")]/@href'
        pricePath = './/div[contains(@class, "flight-operate")]/div[1]/div/span[1]/text()'

        self.logger.info("expect length = " + str(len(response.xpath(rootPath))))
        for div in response.xpath(rootPath):
            try:
                item = MedspiderdemoItem()
                self.logger.info("This is what we are looking at: " + str(div))

                item["price"] = div.xpath(pricePath).extract()
                item["tag"] = div.xpath(namePath).extract()
                # item["link"] = div.xpath(linkPath).extract()

                self.logger.info(count)
                count += 1
                yield item
            except:
                self.logger.info("not this one")
        self.logger.info(count)
