import csv
import re

import pymongo
from pymongo import Connection
connection = Connection()
db = connection.db_hw_mongo


def read_data(csv_file, db):
    """
    Загрузить данные в бд из CSV-файла
    """
    coll = db.artists
    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(csvfile)
        coll.save({reader})
        for artist in coll.find():
            print(artist)


read_data('artists.csv', db)


def find_cheapest(db):
    """
    Отсортировать билеты из базы по возрастанию цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """
    print(db.posts.count())
    for post in db.posts.find({}, {'Цена': 1}).sort():
        print(post)


find_cheapest(db)


def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке, например "Seconds to"),
    и вернуть их по возрастанию цены
    """
    coll = db.artists
    regex = re.compile(r'(^\w*[\s-]\w*|^\w*)')
    sorted_coll = coll.find({'name': regex})
    for names in sorted_coll({}).sort([('name', 1), 'Цена']):
        if name in names:
            print(name)


find_by_name('Seconds', db)
if __name__ == '__main__':
    pass
