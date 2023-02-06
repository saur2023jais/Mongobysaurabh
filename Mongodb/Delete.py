class MongoDelete(object):

    def __init__(self, _client=None, dbName=None, collectionName=None):
        self.client = _client
        self.dbName = dbName
        self.collectionName = collectionName

    def delete_one(self, record={}):
        """
        Insert record in Mongo DB
        :param record: Json
        :return: Bool
        """
        try:
            self.client.mclient[self.dbName][self.collectionName].delete_one(record)
            return True
        except Exception as e:
            print("Error : {} ".format(e))
            return False

    def delete_many(self, record={}):
        """
        Insert record in Mongo DB
        :param record: Json
        :return: Bool
        """
        try:
            self.client.mclient[self.dbName][self.collectionName].delete_many(record)
            return True
        except Exception as e:
            print("Error : {} ".format(e))
            return False

