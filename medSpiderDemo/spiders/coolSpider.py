import scrapy
from scrapy.selector import HtmlXPathSelector
from medSpiderDemo.items import MedspiderdemoItem

class CuteSpider(scrapy.Spider):
    name = 'ticketSpider_v1.0'
    start_urls = ['https://flights.ctrip.com/international/search/round-ord0-hkg0?depdate=2019-03-08_2019-04-12&cabin=y_s&adult=1&child=0&infant=0']

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        #hxs = HtmlXPathSelector(response)
        #titles = response.xpath("//span[@data-component-type = 's-search-results']")
        count = 0
        self.logger.info(response)
        self.logger.info("expect length = " + str(len(response.xpath('//*[@id="app"]/div/div[2]/div[3]/div/div[3]/div'))))
        for div in response.xpath('//*[@id="app"]/div/div[2]/div[3]/div/div[3]/div/span'):
            item = MedspiderdemoItem()
            self.logger.info("This is what we are looking at: " + str(div))

            item["price"] = div.xpath('//span[@class="price"]/text()').extract()
            item["tag"] = div.xpath('//i[@class="arrow-transfer"]/text()').extract()

            airLine = div.xpath('//div[@class="airline-name"]/span/text()').extract()
            flightNum = div.xpath('//div[@class="flight-airline"]/div[@class="plane"]/div[@class="plane"]/span[1]/text()').extract()[0]
            item["link"] = airLine + " " + flightNum

            self.logger.info(count)
            count += 1
            yield item
