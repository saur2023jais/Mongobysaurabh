class MongoUpdate(object):
    def __init__(self, _client=None, dbName=None, collectionName=None):
        self.client = _client
        self.dbName = dbName
        self.collectionName = collectionName

    def update_one_or_more(self, record={}, new_record={}):
        try:
            self.client.mclient[self.dbName][self.collectionName].find_one_and_update(record, {"$set": new_record})
            return True
        except Exception as e:
            print("Error : {} ".format(e))
            return False
