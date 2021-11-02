import scrapy
from scrapy.crawler import CrawlerProcess


class Pagination (scrapy.Spider):
    name = 'pagination'
    start_urls =[]

    custom_settings = {
        'DOWNLOAD_DELAY':0,
        'CONCURRENT_REQUEST_PER_DOMAIN':1
    }



    def __init__(self):
        url='https://quotes.toscrape.com/page/'
        for page in range(1,6):
            self.start_urls.append(url+ str(page))


    def parse(self, response):
        print('respons url:' ,response.url)


process = CrawlerProcess()
process.crawl(Pagination)
process.start(stop_after_crawl=False)