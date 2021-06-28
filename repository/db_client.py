from pymongo import MongoClient


class DataBase():

    def __init__(self):
        self._client = MongoCLient(host='localhost', port=27017)
        self._db = client['restaurants']
