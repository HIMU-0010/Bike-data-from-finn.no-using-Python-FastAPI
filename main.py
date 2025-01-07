import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn

class FinnCode(BaseModel):
    code: int

app =FastAPI()

def upload_to_mongo(data):
    uri = "mongodb://localhost:27017/"
    with MongoClient(uri) as client:
        db = client["finn_data"]
        collection = db["automobile_data"]
        collection.insert_many(data)
        print(f"Uploaded {len(data)} records to MongoDB")

@app.get("/get_data")
def get_data():
    response = requests.get("https://www.finn.no/mobility/search/mc")
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article", class_="relative sf-search-ad card p-10 hover:s-bg-info-subtle focus:s-bg-info-subtle sf-search-ad-legendary")
    data = []
    for article in articles:
        name = article.find("a", class_="sf-search-ad-link s-text! hover:no-underline").text.split(",")[0]
        div = article.find("div", class_="mb-8 flex justify-between whitespace-nowrap font-bold")
        year = div.find_all("span")[0].text
        if div.find_all("span")[1].text.__contains__("km"):
            price = div.find_all("span")[2].text.replace("\xa0","")
        else:
            price = div.find_all("span")[1].text.replace("\xa0","")
        data.append({
            "name": name,
            "year": year,
            "price": price
        })
    
    upload_to_mongo(data)

    return data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)