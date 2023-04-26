import sys
sys.path.append('/home/user/miniconda3/lib/python3.10/site-packages')

import pymongo

def getData():
    client = pymongo.MongoClient("mongodb+srv://muskansingh109080:ddu3V1PXu8hWjMjQ@cluster0.wmf7unk.mongodb.net/")
    db = client['realestate']
    collection = db['pune1']

    data = []

    for document in collection.find():
         
        from .models import Ghar
        # ghar = Ghar(id = document["_id"],name = document['name'],price = document['price'],image = document['image'])
        # ghar.save()
        data.append(document)
        

    return data