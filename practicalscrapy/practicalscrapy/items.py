# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PracticalscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # urls = scrapy.Field()
    name = scrapy.Field()
    form = scrapy.Field()
    company = scrapy.Field()
    unit = scrapy.Field()
    price = scrapy.Field()
    d_price = scrapy.Field()
    generic = scrapy.Field()
    strength = scrapy.Field()
