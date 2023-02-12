# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PaletoScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    down_link = scrapy.Field()
    dead_line = scrapy.Field()
    max_bid = scrapy.Field()
    category = scrapy.Field()
    most_expensive_item_q = scrapy.Field()
    most_expensive_item_price = scrapy.Field()
    most_items_q = scrapy.Field()
    most_items_price = scrapy.Field()
    total_q = scrapy.Field()
    total_price = scrapy.Field()
