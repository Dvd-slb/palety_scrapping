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
        self.cursor = ("""CREATE TABLE IF NOT EXISTS items (
                        name TEXT,
                        link TEXT""")

    def process_item(self, item, spider):
        return item
