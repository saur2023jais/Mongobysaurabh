class Mongo_information(object):

    def __init__(self, _client=None):
        self.client = _client

    def getALllDatabase(self):
        """
        Rreturn all Database Name in Mongo Db
        :return: List
        """
        return self.client.mclient.list_database_names()

    def getAllCollections(self, DbName=None):
        """
        :param DbName: Str
        :return: List
        """
        if DbName is None:
            return []
        else:
            self.client.mclient[DbName].list_collection_names()