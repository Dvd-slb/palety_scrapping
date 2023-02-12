# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import requests
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class PaletoScrapyPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.connection = sqlite3.connect("../data.db")
        # self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS items(
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        link TEXT,
                        down_link TEXT,
                        dead_line DATETIME,
                        max_bid INTEGER,
                        category TEXT,
                        most_expensive_item_q INTEGER,
                        most_expensive_item_price INTEGER,
                        most_expensive_item_desc TEXT,
                        most_items_q INTEGER,
                        most_items_price INTEGER,
                        most_items_desc TEXT,
                        total_q INTEGER,
                        total_price INTEGER
                        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.cursor.execute("SELECT * FROM items WHERE name=?", (item["name"], ))
        if self.cursor.fetchone() is None:
            self.cursor.execute("""INSERT INTO items VALUES (:id, :name, :link, :down_link, :dead_line, :max_bid, :category,
                :most_expensive_item_q, :most_expensive_item_price, :most_expensive_item_desc, :most_items_q,
                :most_items_price, :most_items_desc, :total_q, :total_price)""", {"id": None, "name": item["name"],
                    "link": item["link"], "down_link": item["down_link"], "dead_line": item["dead_line"],
                    "max_bid": item["max_bid"], "category": item["category"], "most_expensive_item_q": False,
                    "most_expensive_item_price": False, "most_expensive_item_desc": False, "most_items_q": False,
                    "most_items_price": False, "most_items_desc": False, "total_q": False, "total_price": False})

        self.connection.commit()


# _______________ POSTUP NA STAŽENÍ XLSX SOUBORU S DETAILY JEDNOTLIVÝCH PALET ________________
# cursor.execute("SELECT down_link, name FROM items")
# for f in cursor.fetchall():
#     url = f[0]
#     name = f[1]
#     file = requests.get(url)
#     with open(f"../box_description/{name}.xlsx", "wb") as box_details:
#         box_details.write(file.content)


# _________________________________  PŘEVOD   NA   DATATIME  _________________________________
# date_string = '14. 2. 2023 18:44:00'
# date_format = "%d. %m. %Y %H:%M:%S"
# date_parsed = datetime.strptime(date_string, date_format)
# print(date_parsed)