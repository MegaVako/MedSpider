# MedSpider
med-level spider

To run docker: docker run -p 8050:8050 scrapinghub/splash

To run spider: scrapy crawl xcSpider_v1.0 -s ROBOTSTXT_OBEY=False -o <output_Name>.json

Notice

  setting.py might not apply to spiders other than xcSpider_v1.0
  
  Helpful sites:
  
  Problem with /etc/machine-id:
  
  http://www.torkwrench.com/2011/12/16/d-bus-library-appears-to-be-incorrectly-set-up-failed-to-read-machine-uuid-failed-to-open-varlibdbusmachine-id/
  
  Dynamic/JavaScript content:
  
  https://stackoverflow.com/questions/30345623/scraping-dynamic-content-using-python-scrapy
  
  Possible SPLASH_URL problem
  
  https://stackoverflow.com/questions/41610403/scrapy-splash-connection-refused
  
  My scrapinghub:
  
  https://app.scrapinghub.com/p/375850/jobs
  
  Further scrapy learning
  
  https://blog.scrapinghub.com/2016/11/24/how-to-build-your-own-price-monitoring-tool
  
  Main xpath info page
  
  https://doc.scrapy.org/en/xpath-tutorial/topics/xpath-tutorial.html
  
  Info about crawling/robot.txt
  
  https://canicrawl.com/
  
  Alternative approches about dynamic content
  
  https://stackoverflow.com/questions/8550114/can-scrapy-be-used-to-scrape-dynamic-content-from-websites-that-are-using-ajax
  
  https://blog.scrapinghub.com/2015/03/02/handling-javascript-in-scrapy-with-splash
  
  Proxy Info
  
  https://stackoverflow.com/questions/4710483/scrapy-and-proxies
