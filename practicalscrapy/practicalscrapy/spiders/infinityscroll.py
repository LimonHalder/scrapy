import json
from  ..items import PracticalscrapyItem
from scrapy.crawler import CrawlerProcess
import scrapy
import json


from ..items import PracticalscrapyItem


class QuoteScrollSpider(scrapy.Spider):
    current_pages = 1
    name = "scroll"
    #api_url = 'https://api.arogga.com/v1/medicines/?cat_id=20&page=&f=web&b=Chrome&v=95.0.4638.54&os=Windows&osv=10'
    #start_urls = {api_url.format(1)}
    start_urls=[]
    def __init__(self):

        #ex = '&f=web&b=Chrome&v=95.0.4638.54&os=Windows&osv=10'
        url = 'https://api.arogga.com/v1/medicines/?cat_id=13&page='
        for page in range(1, 10):
            self.start_urls.append(url + str(page))


    def parse(self, response):
        data = json.loads(response.body)
        items = PracticalscrapyItem()
        for quote in data['data']:
            name = quote["name"]
            form=quote["form"]
            company =quote["company"]
            unit =quote["unit"]
            price=quote['price']
            d_price=quote['d_price']
            generic = quote["generic"]
            strength = quote['strength']


            items['name']=name
            items['form'] =form

            items['company'] = company
            items['unit'] = unit
            items['price'] =price
            items['d_price'] =d_price
            items['generic'] = generic

            items['strength'] = strength


            yield items

process = CrawlerProcess()
process.crawl(QuoteScrollSpider)
process.start(stop_after_crawl=False)
