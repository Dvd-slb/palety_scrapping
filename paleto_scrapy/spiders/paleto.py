import scrapy
from ..items import PaletoScrapyItem


class PaletoSpider(scrapy.Spider):
    name = 'paleto'
    # allowed_domains = ['paleto.eu']
    start_urls = ['https://paleto.eu/bezici-aukce/']

    def parse(self, response, **kwargs):
        # items = PaletoScrapyItem()

        stage = response.css("div.products-wrapper")

        for box in stage:
            # name = box.css(".ean::text").get()
            link = box.css("h3 a::attr(href)").get()

            yield response.follow(link, callback=self.detail_parse)
            # items["name"] = name
            # items["link"] = link
            #
            # yield items

    def detail_parse(self, response):
        # print("_______________________čůůůůůůůůůůůůůůůůůůůůůůůůůůůůůůůůůůssssssssss______________________________")
        items = PaletoScrapyItem()

        name_confirm = response.css("h1 .ean::text").get()
        link = response.url

        current_link = response.css("div.wcpoa_attachment a::attr(href)").get()
        id_to_change = response.css("div.wcpoa_attachment a::attr(href)").re("id=....")[0][3:]
        new_id = str(int(response.css("div.wcpoa_attachment a::attr(href)").re("id=....")[0][3:]) + 1)
        down_link = current_link.replace(id_to_change, new_id).replace("dcdbz6bb06wy1", "4lwl92q9s0axw")
        # print(new_link)

        try:
            date_info = response.css("h5.uwa_auction_end_time::text").getall()[1].split()
            dead_line = f"{date_info[0]} {date_info[1]} {date_info[2]} {date_info[3]}"
        except:
            date_info = response.css(".uwa_auction_product_end_time::text").getall()[1].split()
            dead_line = f"{date_info[0]} {date_info[1]} {date_info[2]} {date_info[3]}"

        max_bid = ""
        bid_info = response.css("span.woo-ua-auction-price bdi::text").get()
        for letter in bid_info:
            if letter.isdigit():
                max_bid += letter
            else:
                continue

        items["name"] = name_confirm
        items["link"] = link
        items["dead_line"] = dead_line
        items["max_bid"] = int(max_bid)
        items["down_link"] = down_link
        yield items



# class DetailSpider(scrapy.Spider):
#     name = "detail"
#
#     start_urls = []
#
#     def parse(self, response):
#         details = DetailScrapyItem()
#         down_link = response.css("div.wcpoa_attachment a::attr(href)").get()
#         id_to_change = response.css("div.wcpoa_attachment a::attr(href)").re("id=....")[0][3:]
#         new_id = str(int(response.css("div.wcpoa_attachment a::attr(href)").re("id=....")[0][3:]) + 1)
#         new_link = down_link.replace(id_to_change, new_id).replace("dcdbz6bb06wy1", "4lwl92q9s0axw")
#         details["down_link"] = new_link
#         yield details
