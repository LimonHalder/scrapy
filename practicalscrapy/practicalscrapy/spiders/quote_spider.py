import scrapy

#from ..items import PracticalscrapyItem



class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 66
    start_urls=[
        'http://www.squarepharma.com.bd/products-by-tradename.php?type=pharma&char=A'
]

    def parse(self, response):
        #items = PracticalscrapyItem()

        all_div_quotes=response.css('.col-xs-12 col-sm-4 col-md-4 col-lg-4')
        for quotes in all_div_quotes:
            #title =quotes.css('span.text::text').extract()
            #author=quotes.css('.author::text').extract()
            urls = quotes.css(" .imgth-holder a").xpath("@href").extract()

            #items['title'] = title
            #items['author'] = author
            #items['urls'] = urls
            #yield items
            for url in urls:
                url =response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)
#next_page = 'https://quotes.toscrape.com/page/'+ chr(QuoteSpider.page_number)+'/'
        next_page = 'http://www.squarepharma.com.bd/products-by-tradename.php?type=pharma&char='+ chr(QuoteSpider.page_number)+'/'
        if QuoteSpider.page_number < 91:
            QuoteSpider.page_number +=1
           # QuoteSpider.page_number = chr(ord(QuoteSpider.page_number) + 1)
            yield response.follow(next_page, callback=self.parse)


    def parse_details(self,response):
        raw_images_urls = response.css('< img ::attr(src)').getall()
        clean_image_urls = []
        for img_url in raw_images_urls:
            clean_image_urls.append(response.urljoin(img_url))

        yield {
            'image_urls': clean_image_urls
        }

       #yield {
           #'name': response.css("h3.author-title").extract()
       #}