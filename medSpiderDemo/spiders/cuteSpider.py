import scrapy
from scrapy.selector import HtmlXPathSelector
from medSpiderDemo.items import MedspiderdemoItem

class CuteSpider(scrapy.Spider):
    name = 'schoolSpider_v1.3'
    allowed_domains = ["4icu.org"]
    start_urls = ['https://www.4icu.org/us/']

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        #hxs = HtmlXPathSelector(response)
        #titles = response.xpath("//span[@data-component-type = 's-search-results']")
        count = 0
        self.logger.info("expect length = " + str(len(response.xpath('//table[@class="table table-hover"]/tbody/tr'))))
        for tr in response.xpath('//table[@class="table table-hover"]/tbody/tr'):
            self.logger.info(str(tr))
            item = MedspiderdemoItem()
            # /html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[1]/b
            self.logger.info("This is what we are looking at: " + str(tr))
            item["price"] = tr.xpath('./td[1]/b/text()').extract()
            item["tag"] = tr.xpath('./td[2]/a/text()').extract()
            item["link"] = tr.xpath('./td[2]/a/@href').extract()
            self.logger.info(count)
            count += 1
            yield item
