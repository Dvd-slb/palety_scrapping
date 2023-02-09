import scrapy
from ..items import PaletoScrapyItem

class PaletoSpider(scrapy.Spider):
    name = 'paleto'
    # allowed_domains = ['paleto.eu']
    start_urls = ['https://paleto.eu/bezici-aukce/']

    def parse(self, response):
        items = PaletoScrapyItem()

        stage = response.css("div.products-wrapper")

        for box in stage:
            id = box.css(".ean::text").get()
            link = box.css("h3 a::attr(href)").get()

            items["id"] = id
            items["link"] = link

            yield items
