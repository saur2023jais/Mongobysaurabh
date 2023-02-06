try:
    import os
    import pandas as pd
    import sys
    import io
    import pymongo
    import json
    from pymongo import MongoClient
    from bson.objectid import ObjectId
    from Insert import MongoInsert
    from Delete import MongoDelete
    from Mongodb.import_csv import MongoDB_csv
    from Update import MongoUpdate
    from Information_db import Mongoinformation

    print("All Modules loaded ")
except Exception as e:
    print("Error : {} ".format(e))


class Singleton(type):
    """This would be a Singleton  Design pattern """

    _instance = {}

    def __call__(cls, *args, **kwargs):  # dunder call
        """Creates only one instance of the class """
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class Settings(metaclass=Singleton):
    def __init__(self, host=None, maxPoolSize=50, port=27010):
        self.host = host
        self.maxPoolSize = maxPoolSize
        self.port = port


class Client(metaclass=Singleton):

    def __init__(self, _settings=None):
        self.settings = _settings
        self.mclient = MongoClient(host=self.settings.host,
                                   port=self.settings.port,
                                   maxPoolSize=self.settings.maxPoolSize)


def main():
    url = "mongodb://root:rootpassword@localhost:27017"

    # Creates a instance of settings class
    _settings = Settings(host=url)

    # creates a single instance of client object
    _client = Client(_settings=_settings)

    ch = 'y'
    while ch == 'y' or ch == 'Y' or ch == 'yes':

        print("Enter Choice \n 1:Insert \n 2:Delete \n 3:Import_csv_file \n 4:Update \n 5:Find")
        x = int(input())

        match x:
            case 1:
                _record = {"name": "Rajpal Yadav", "address": "Delhi"}
                dbName = "person"
                collectionName = "names"
                _helper = MongoInsert(_client=_client, dbName=dbName, collectionName=collectionName)
                res = _helper.insert_one(record=_record)
                print(res)
            case 2:
                _record = {"_id": ObjectId("63de6461be55cc9f9df91753")}
                dbName = "person"
                collectionName = "names"
                _helper = MongoDelete(_client=_client, dbName=dbName, collectionName=collectionName)
                res = _helper.delete_one(record=_record)
                print(res)
            case 3:
                dbName = 'Dataset'
                collectionName = 'EnergyConsumption'
                _helper = MongoDB_csv(_client=_client, dbName=dbName, collectionName=collectionName)
                res = _helper.InsertData(path="Mongodb/netflix_titles.csv")
                print(res)
            case 4:
                _record = {"_id": ObjectId("63e08a94f5053a4fa52f1b43")}
                dbName = "person"
                collectionName = "names"
                _new_record = {"name": "Shivam Verma", "address": "Nainital"}
                _helper = MongoUpdate(_client=_client, dbName=dbName, collectionName=collectionName)
                res = _helper.update_one_or_more(record=_record, new_record=_new_record)
                print(res)

        ch = input("If you want to continue click y/yes:")

    _client.mclient.close()
    print("Connection Close")


if __name__ == "__main__":
    main()

