import pandas as pd


class MongoDB_csv(object):

    def __init__(self, _client=None, dbName=None, collectionName=None):
        self.client = _client
        self.dbName = dbName
        self.collectionName = collectionName
        self.DB = self.client.mclient[self.dbName]
        self.collection = self.DB[self.collectionName]

    def InsertData(self, path=None):
        """
        :param path: Path os csv File
        :return: None
        """
        try:
            df = pd.read_csv(path)
            data = df.to_dict('records')
            self.collection.insert_many(data, ordered=False)
            return True
        except Exception as e:
            print("Error : {} ".format(e))
            return False


