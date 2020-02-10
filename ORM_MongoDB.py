import csv
from pymongo import MongoClient
import re
from datetime import datetime
import time
connection = MongoClient()
db = connection.db_hw_mongo


def read_data(csv_file, database):

    with open(csv_file, 'r', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row_dict = {'Исполнитель': row[0],
                        "Цена": int(row[1]),
                        "Место": row[2],
                        "Дата": datetime.strptime(row[3], '%d.%m')}
            database.artist.insert_one(row_dict)


read_data('artists.csv', db)


def find_cheapest(database):

    return database.artist.find().sort([('Цена', 1)])


print('Самый дешевый билет:', find_cheapest(db))


def find_by_name(name, database):

    regex = re.compile(name)
    return database.artist.find({'Исполнитель': regex})


print(find_by_name('Seconds', db))
