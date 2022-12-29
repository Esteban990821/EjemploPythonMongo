import pymongo
import certifi

ca = certifi.where()


client = pymongo.MongoClient("mongodb+srv://mintic-academic:XwEGDZmG1qEw5B2b@cluster0.h0qmqbi.mongodb.net/db-academic-register?retryWrites=true&w=majority",tlsCAFile=ca)


db = client.test
print(db)

baseDatos = client["db-academic-register"]
print(baseDatos.list_collection_names())