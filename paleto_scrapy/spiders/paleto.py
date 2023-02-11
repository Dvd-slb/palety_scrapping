import scrapy
from ..items import PaletoScrapyItem

class PaletoSpider(scrapy.Spider):
    name = 'paleto'
    # allowed_domains = ['paleto.eu']
    start_urls = ['https://paleto.eu/bezici-aukce/']

    def parse(self, response, **kwargs):
        items = PaletoScrapyItem()

        stage = response.css("div.products-wrapper")

        for box in stage:
            id = box.css(".ean::text").get()
            link = box.css("h3 a::attr(href)").get()

            yield response.follow(link, callback=self.detail_parse)
            items["id"] = id
            items["link"] = link

            yield items

    def detail_parse(self, response):
        # print("_______________________čůůůůůůůůůůůůůůůůůůůůůůůůůůůůůůůůůůssssssssss______________________________")
        items = PaletoScrapyItem()
        down_link = response.css("div.wcpoa_attachment a::attr(href)").get()
        id_to_change = response.css("div.wcpoa_attachment a::attr(href)").re("id=....")[0][3:]
        new_id = str(int(response.css("div.wcpoa_attachment a::attr(href)").re("id=....")[0][3:]) + 1)
        new_link = down_link.replace(id_to_change, new_id).replace("dcdbz6bb06wy1", "4lwl92q9s0axw")
        # print(new_link)
        items["down_link"] = new_link
        yield items

        # items["down_link"] = new_link
        # yield items


class DetailSpider(scrapy.Spider):
    name = "detail"

    start_urls = []

    def parse(self, response):
        details = DetailScrapyItem()
        down_link = response.css("div.wcpoa_attachment a::attr(href)").get()
        id_to_change = response.css("div.wcpoa_attachment a::attr(href)").re("id=....")[0][3:]
        new_id = str(int(response.css("div.wcpoa_attachment a::attr(href)").re("id=....")[0][3:]) + 1)
        new_link = down_link.replace(id_to_change, new_id).replace("dcdbz6bb06wy1", "4lwl92q9s0axw")
        details["down_link"] = new_link
        yield details
