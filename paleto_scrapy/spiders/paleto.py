import requests
import scrapy
from datetime import datetime
from ..items import PaletoScrapyItem


class PaletoSpider(scrapy.Spider):
    name = 'paleto'
    start_urls = ['https://paleto.eu/bezici-aukce/']

    def parse(self, response, **kwargs):

        # stage = response.css("div.products-wrapper")
        # for box in stage:
        #     link = box.css("h3 a::attr(href)").get()
        #     yield response.follow(link, callback=self.detail_parse)
        link = 'https://paleto.eu/a/s1581/'
        yield response.follow(link, callback=self.detail_parse)

    def detail_parse(self, response):
        items = PaletoScrapyItem()

        name = response.css("h1 .ean::text").get()
        link = response.url

        dead_line = self.dead_line_define(response)
        max_bid = self.max_bid_define(response)
        category = self.category_define(response)
        down_link = self.down_link_define(response)

        # file = requests.get(down_link)
        # with open(f"../../box_description/{name}.xlsx", "wb") as f:
        #     f.write(file.content)

        # file = requests.get(down_link)
        # open(f"../../box_description/{name}.xlsx", "wb").write(file.content)

        items["name"] = name
        items["link"] = link
        items["dead_line"] = dead_line
        items["max_bid"] = int(max_bid)
        items["category"] = category
        items["down_link"] = down_link
        yield items

    def dead_line_define(self, response):
        months_cz = ["ledna", "února", "března", "dubna", "května", "června", "července", "srpna", "září", "října",
                     "listopadu", "prosince"]
        date_format = "%d. %m. %Y %H:%M:%S"
        index = 1
        try:
            date_info = response.css("h5.uwa_auction_end_time::text").getall()[1].split()
            for month in months_cz:
                if date_info[1] == month:
                    date_info[1] = f"{index}."
                index += 1
            dead_line = f"{date_info[0]} {date_info[1]} {date_info[2]} {date_info[3]}:00"

            # dead_line_str = f"{date_info[0]} {date_info[1]} {date_info[2]} {date_info[3]}"
            # dead_line = datetime.strptime(dead_line_str, date_format)

        except IndexError:
            date_info = response.css(".uwa_auction_product_end_time::text").getall()[1].split()
            for month in months_cz:
                if date_info[1] == month:
                    date_info[1] = f"{index}."
                index += 1
            dead_line = f"{date_info[0]} {date_info[1]} {date_info[2]} {date_info[3]}:00"

            # dead_line_str = f"{date_info[0]} {date_info[1]} {date_info[2]} {date_info[3]}"
            # dead_line = datetime.strptime(dead_line_str, date_format)

        return dead_line

    def max_bid_define(self, response):
        max_bid = ""
        bid_info = response.css("span.woo-ua-auction-price bdi::text").get()
        for letter in bid_info:
            if letter.isdigit():
                max_bid += letter
            else:
                continue
        return max_bid

    def category_define(self, response):
        category = ""
        category_source = response.css("h1 span nobr::text").getall()[0], response.css("h1 span::text").getall()[-1]
        for l in category_source[1]:
            if l.isdigit():
                category = category_source[0]
                break
            else:
                category = category_source[0] + category_source[1]
        return category

    def down_link_define(self, response):
        current_link = response.css("div.wcpoa_attachment a::attr(href)").get()
        id_to_change = response.css("div.wcpoa_attachment a::attr(href)").re("id=....")[0][3:]
        new_id = str(int(response.css("div.wcpoa_attachment a::attr(href)").re("id=....")[0][3:]) + 1)
        down_link = current_link.replace(id_to_change, new_id).replace("dcdbz6bb06wy1", "4lwl92q9s0axw")
        return down_link
