import requests

URL = "https://keyword-analysis.p.rapidapi.com/api/query/SimilarQueries"
HEADERS = {
    "x-rapidapi-host": "keyword-analysis.p.rapidapi.com",
    "x-rapidapi-key": "Your-X-RapidAPI-Key"
}

querystring = {"q": "john wick 3"}

response = requests.get(URL, headers=HEADERS, params=querystring).json()
print(response)

for item in response:
    name = item["name"]
    score = item["score"]

    print("name: {}, score: {}.".format(name, score))
