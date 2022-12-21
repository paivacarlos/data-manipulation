#importing a mongoClint to connect a mongoDb app
from pymongo import MongoClient
import datetime

#connect database
conn = MongoClient('localhost', 27017)
type(conn)

#only instance od MongoDB can support any databases
#create a database
db = conn.firstdb
type(db)

#one collection is a group documents stored in MongoDB
colletion = db.firstdb
type(colletion)

post1 = {
    "code": "1989",
    "prod_name": "Carlos Paiva",
    "gender": "male",
    "register_date": datetime.datetime.utcnow()
}

type(post1)

colletion = db.posts
post_id = colletion.insert_one(post1)
post_id.inserted_id
post_id

post2 = {
    "code": "1992",
    "prod_name": "Pati Scalco",
    "gender": "female",
    "register_date": datetime.datetime.utcnow()
}

colletion = db.posts
post_id = colletion.insert_one(post2).inserted_id
post_id

#function find return a cursor and we can navegate on the data
for post in colletion.find():
    print(post)

#verify db_name
print(db.name)

#verify collections avalible
print(db.collection_names)