from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(
    "mongodb+srv://Edison:y1m2y3gh@cluster0.xxw2u.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)
db=client.test
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
