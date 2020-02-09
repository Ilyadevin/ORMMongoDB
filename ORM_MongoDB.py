import csv
from pymongo import MongoClient
import re

connection = MongoClient()
db = connection.db_hw_mongo


def read_data(csv_file, database):

    with open(csv_file, 'r', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row_dict = {'Исполнитель': row[0], "Цена": int(row[1]), "Место": row[2], "Дата": float(row[3])}
            database.artist.insert_many(row_dict)


read_data('artists.csv', db)


def find_cheapest(database):

    database.artist.find()
    database.artist.find().sort([('Цена', 1)])


find_cheapest(db)


def find_by_name(name, database):

    regex = re.compile(r'(^\w*[\s-]\w*|^\w*)')
    return database.artist.find({'Исполнитель': {regex: name}})


find_by_name('Seconds', db)

if __name__ == '__main__':
    pass
