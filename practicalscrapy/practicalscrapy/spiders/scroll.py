import scrapy


class ImageDownloader(scrapy.Spider):
    page_number=66
    name = 'image'
    start_urls = ['https://bengalremediesltd.com/product1.php?idn=3']

    def parse(self, response):
        raw_images_urls = response.css('a img::attr(src)').getall()
        clean_image_urls = []
        for img_url in raw_images_urls:
            clean_image_urls.append(response.urljoin(img_url))

        yield {
            'image_urls': clean_image_urls
            }
        #next_page = 'http://www.squarepharma.com.bd/products-by-tradename.php?type=pharma&char='+ chr(ImageDownloader.page_number)+ ''
        #next_page = 'https://quotes.toscrape.com/page/'+ str(ImageDownloader.page_number) + '/'
        #if ImageDownloader.page_number < 91:
           # ImageDownloader.page_number +=1
           # QuoteSpider.page_number = chr(ord(QuoteSpider.page_number) + 1)
        #yield response.follow(next_page, callback=self.parse)

