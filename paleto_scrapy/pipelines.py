# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class PaletoScrapyPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        # self.connection = sqlite3.connect("data.db")
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS items (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        link TEXT,
                        down_link TEXT,
                        dead_line DATETIME,
                        max_bid INTEGER,
                        category TEXT,
                        most_expensive_item_q INTEGER,
                        most_expensive_item_price INTEGER,
                        most_items_q INTEGER,
                        most_items_price INTEGER,
                        total_q INTEGER,
                        total_price INTEGER
                        )""")
        self.connection.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.cursor.execute("SELECT * FROM items WHERE name=?", (item["name"]))
        if self.cursor.fetchone() is None:
            print("ok")
        else:
            print("not ok")

        self.connection.commit()


# _________________________________  PŘEVOD   NA   DATATIME  _________________________________
# date_string = '14. 2. 2023 18:44'
# date_format = "%d. %m. %Y %H:%M"
# date_parsed = datetime.strptime(date_string, date_format)
# print(date_parsed)