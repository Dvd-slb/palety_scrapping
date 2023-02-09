# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PaletoScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    link = scrapy.Field()
    deadline = scrapy.Field()
    max_bid = scrapy.Field()
    category = scrapy.Field()
    most_expensive_item = scrapy.Field()
    most_items_definition = scrapy.Field()
    most_items_number = scrapy.Field()
    total_q = scrapy.Field()
    total_price = scrapy.Field()
