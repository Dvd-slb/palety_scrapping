import sqlite3
from dateutil.parser import parse
from datetime import datetime

date_string = '14. 2. 2023 18:44'
date_format = "%d. %m. %Y %H:%M"
date_parsed = datetime.strptime(date_string, date_format)
print(date_parsed)



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