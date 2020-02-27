import csv
from pymongo import MongoClient
import re
from datetime import datetime

connection = MongoClient()
db = connection.db_hw_mongo


class MongoDB:
    def __init__(self, csv_file, database, name):
        self.csv_file = csv_file
        self.database = database
        self.name = name

    def read_data(self):
        with open(self.csv_file, 'r', encoding='utf8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                row_dict = {'Исполнитель': row[0],
                            "Цена": int(row[1]),
                            "Место": row[2],
                            "Дата": datetime.strptime(row[3], '%d.%m')}
                self.database.artist.insert_one(row_dict)

    def find_cheapest(self):
        return self.database.artist.find().sort([('Цена', 1)])

    def find_by_name(self):
        regex = re.compile(self.name)
        return self.database.artist.find({'Исполнитель': regex})


data = MongoDB(csv_file='artists.csv', database=db, name=input("Введите название группы "))
data.read_data()
print(data.find_cheapest())
print(data.find_by_name())
