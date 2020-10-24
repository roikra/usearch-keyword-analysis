import requests

URL = "https://keyword-analysis.p.rapidapi.com/api/query/QueryKeywords"
HEADERS = {
    "x-rapidapi-host": "keyword-analysis.p.rapidapi.com",
    "x-rapidapi-key": "Your-X-RapidAPI-Key"
}

querystring = {"q":"cyberia game review"}

response = requests.get(URL, headers=HEADERS, params=querystring)
print(response.text)
