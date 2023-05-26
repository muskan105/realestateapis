import sys
sys.path.append('/home/user/miniconda3/lib/python3.10/site-packages')

import pymongo

def getData():
    client = pymongo.MongoClient("mongodb+srv://muskansingh109080:ddu3V1PXu8hWjMjQ@cluster0.wmf7unk.mongodb.net/")
    db = client['realestate']
    collection = db['pune1']

    data = collection.find()

    # change price to int
    def getPrice(d11):
        price_str = d11.get("price").split(" ")
        price_amount = price_str[0][1:]
        price_denomiation = price_str[1]
        final_price = 0
        if price_denomiation == "Lac":
            final_price = float(price_amount) * 100000
        elif price_denomiation == "Cr.":
            final_price = float(price_amount) * 10000000
        final_price = int(final_price)
        return final_price
    
    def getBhk(d11):
        bhk = d11.get("name").split(" ")
        bhk = bhk[0]
        return bhk
    # print(bhk)
    def getPlace(d11):
        place = d11.get("name").split(",")
        place = place[0].split("in")
        place = place[-1].strip()
        return place

    list_data = []
    # print('len',len(data))
    for i in data:
        from .models import Ghar
        ghar = Ghar(
            id = i["_id"],
            name = i['name'],
            image = i['image'],
            price_amount = getPrice(i),
            bhk = getBhk(i),
            place = getPlace(i)
            )
        ghar.save()