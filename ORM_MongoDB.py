import csv
import re

import pymongo
from mongoengine import connect

db = connect("db_hw_mongo")


def read_data(csv_file, database):
    """
    Загрузить данные в бд из CSV-файла
    """
    collecion = database['artists']
    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        csvfiles_int = [map(int, row) for row in csv.reader(csvfile, delimiter=',')]
        reader = csv.DictReader(csvfile)
        collecion.insert_one({'Исполнитель': reader, 'Цена': reader, 'Место': reader, 'Дата': reader})


read_data('artists.csv', db)


def find_cheapest(database):
    """
    Отсортировать билеты из базы по возрастанию цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """
    database.artists.find().sort({'Цена': 1})


find_cheapest(db)


def find_by_name(name, database):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке, например "Seconds to"),
    и вернуть их по возрастанию цены
    """
    regex = re.compile(r'(^\w*[\s-]\w*|^\w*)')
    with open('artists.csv', encoding='utf8') as f:
        if name in regex:
            name_finded = name
            database.artists.find({'name': name_finded}).sort({'Цена': 1})
        else:
            pass


find_by_name('Seconds', db)

if __name__ == '__main__':
    pass
