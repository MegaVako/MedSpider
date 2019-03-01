import scrapy
from scrapy.selector import HtmlXPathSelector
from medSpiderDemo.items import MedspiderdemoItem

class StrongSpider(scrapy.Spider):
    name = 'amazonSpider_v1.0'
    start_urls = ['https://www.amazon.com/s?k=keyboard&ref=nb_sb_noss']

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        #hxs = HtmlXPathSelector(response)
        #titles = response.xpath("//span[@data-component-type = 's-search-results']")
        count = 0
        self.logger.info(response)
        # temp = MedspiderdemoItem()
        # temp["tag"] = response.text
        # yield temp

        namePath = './/span[contains(@class, "a-size-medium a-color-base a-text-normal")]/text()'
        rootPath = '//div[contains(@class, "a-section a-spacing-medium")]'
        rootPath2 = '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div'
        # path2 = '//a[contains(@class,'question')]'

        linkPath = './/a[contains(@class,"a-link-normal a-text-normal")]/@href'
        pricePath = './/span[contains(@class, "a-offscreen")]/text()'

        self.logger.info("expect length = " + str(len(response.xpath(rootPath2))))
        for div in response.xpath(rootPath2):
            try:
                item = MedspiderdemoItem()
                self.logger.info("This is what we are looking at: " + str(div))

                item["price"] = div.xpath(pricePath).extract()
                item["tag"] = div.xpath(namePath).extract()
                item["link"] = div.xpath(linkPath).extract()

                self.logger.info(count)
                count += 1
                yield item
            except:
                self.logger.info("not this one")
        self.logger.info(count)
