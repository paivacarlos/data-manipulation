import pymongo

#creating a standar connection
client_con = pymongo.MongoClient()

#list availeble mongoDB
print(client_con.list_database_names())

#define db object
db = client_con.firstdb

#lis avalible collections
print(db.list_collection_names())

#creating a new collection
#db.create_collection("my_collection")
print(db.list_collection_names())

#inserting a document in the collection created
db.my_collection.insert_one({
    "title": "MongoDB with Python",
    "description": "MongoDB is database NoSql",
    "by": "Data Science Acadamy",
    "url": "http://exemplo.com.br",
    "tafs": ['mongoDB', 'database', 'NoSQL'],
    "likes": 189
})

#return a created document
print(db.my_collection.find_one())

#connect a collection
col = db["posts"]

#counting how documents have
#print(col.count())

#finding a one document
redoc = col.find_one()
print(redoc)