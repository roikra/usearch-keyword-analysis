import requests

URL = "https://keyword-analysis.p.rapidapi.com/api/query/PopularDomainsForQuery"

HEADERS = {
    "x-rapidapi-host": "keyword-analysis.p.rapidapi.com",
    "x-rapidapi-key": "Your-X-RapidAPI-Key"
}

querystring = {"q": "taylor swift"}

response = requests.get(URL, headers=HEADERS, params=querystring).json()

for item in response:
    name = item["name"]
    score = item["score"]

    print("name: {}, score: {}.".format(name, score))
