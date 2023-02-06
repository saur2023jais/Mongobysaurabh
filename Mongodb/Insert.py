class MongoInsert(object):

    def __init__(self, _client=None, dbName=None, collectionName=None):
        self.client = _client
        self.dbName = dbName
        self.collectionName = collectionName

    def insert_one(self, record={}):
        """
        Insert record in Mongo DB
        :param record: Json
        :return: Bool
        """
        try:
            self.client.mclient[self.dbName][self.collectionName].insert_one(record)
            return True
        except Exception as e:
            print("Error : {} ".format(e))
            return False

    def insert_many(self, record={}):
        """
        Insert record in Mongo DB
        :param record: Json
        :return: Bool
        """
        try:
            self.client.mclient[self.dbName][self.collectionName].insert_many(record)
            return True
        except Exception as e:
            print("Error : {} ".format(e))
            return False

    def insert_pandas_df(self, df=None):
        """

        :param df: Pandas DF
        :return: Bool
        """

        try:
            self.client.mclient[self.dbName][self.collectionName].insert_many(df.to_dict(), ordered=False)
            return True
        except Exception as e:
            return False
