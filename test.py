import sqlite3
import requests
from dateutil.parser import parse
from datetime import datetime

connection = sqlite3.connect("../data.db")
# connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("SELECT * FROM items")
print(cursor.fetchall())
cursor.execute("SELECT * FROM items")
print(len(cursor.fetchall()))


# _________ STAŽENÍ SOUBORU Z LINKU Z DATABÁZE ________
# cursor.execute("SELECT down_link, name FROM items")
# for f in cursor.fetchall():
#     url = f[0]
#     name = f[1]
#     file = requests.get(url)
#     with open(f"../box_description/{name}.xlsx", "wb") as box_details:
#         box_details.write(file.content)

# cursor.execute("SELECT * FROM items WHERE name=?", ("S1955", ))
# print(cursor.fetchall())

# cursor.execute("SELECT down_link FROM items")
# down_link = cursor.fetchall()
# cursor.execute("SELECT name FROM items")
# name = cursor.fetchall()
# print(down_link)
# print(name)
# file = requests.get(cursor.fetchall()

connection.commit()
connection.close()

# cursor.execute("""CREATE TABLE IF NOT EXISTS items(
#                         id INTEGER PRIMARY KEY,
#                         name TEXT,
#                         link TEXT,
#                         down_link TEXT,
#                         dead_line DATETIME
#                         )""")
                        # max_bid INTEGER,
                        # category TEXT,
                        # most_expensive_item_q INTEGER,
                        # most_expensive_item_price INTEGER,
                        # most_items_q INTEGER,
                        # most_items_price INTEGER,
                        # total_q INTEGER,
                        # total_price INTEGER
                        # )""")

# cursor.execute("PRAGMA table_info(items)")
# column_names = [row[1] for row in cursor.fetchall()]
# print(column_names)

# cursor.execute("ALTER TABLE items ADD name TEXT")

# cursor.execute("INSERT INTO items VALUES (:id, :name, :link, :down_link, :dead_line)", {"id": None, "name": "kokot", "link": "neznam",
#                                                                                    "down_link": False, "dead_line": False})

# cursor.execute("INSERT INTO items VALUES (:id, :name, :link, :down_link, :dead_line)", {"id": None, "name": "yep", "link": "vim",
#                                                                                    "down_link": False, "dead_line": "nikdy"})

# cursor.execute("SELECT * FROM items")
# print(cursor.fetchall())
# cursor.execute("SELECT * FROM items")
# print(len(cursor.fetchall()))
#
# connection.commit()
# connection.close()

# date_string = '14. 2. 2023 18:44:00'
# date_format = "%d. %m. %Y %H:%M:%S"
# date_parsed = datetime.strptime(date_string, date_format)
# print(date_parsed)
#
# hm = date_parsed.strftime(date_format)
# print(hm)


# months_cz = ["ledna", "února", "března", "dubna", "května", "června", "července", "srpna", "září", "října", "listopadu",
#              "prosince"]
# index = 1
# date_origin = "12. srpna 2023 18:32".split()
# for month in months_cz:
#     if date_origin[1] == month:
#         date_origin[1] = f"{index}."
#     index += 1
#
# date_string = ""
# for c in date_origin:
#     date_string += c + " "

# print(date_string)




# parsed_date = parse(date_string)
# print(parsed_date)

# connection = sqlite3.connect(":memory:")
# cursor = connection.cursor()
#
# cursor.execute("""CREATE TABLE IF NOT EXISTS items (
#                 name TEXT,
#                 link TEXT,
#                 )""")
#
# cursor.execute("SELECT name FROM items")
#
# print(cursor.fetchall())