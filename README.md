# Using Python to call the Search APIs:
  - ##### Popular Sites For Query
  - ##### Query keywords
  - ##### Similar Queries


## Popular Sites For Query
```sh
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

```


## Query keywords
```sh
import requests

URL = "https://keyword-analysis.p.rapidapi.com/api/query/QueryKeywords"
HEADERS = {
    'x-rapidapi-host': "keyword-analysis.p.rapidapi.com",
    'x-rapidapi-key': "Your-X-RapidAPI-Key"
}

querystring = {"q":"cyberia game review"}

response = requests.get(URL, headers=HEADERS, params=querystring)
print(response.text)
```



## Similar Queries
```sh
import requests

URL = "https://keyword-analysis.p.rapidapi.com/api/query/SimilarQueries"
HEADERS = {
    'x-rapidapi-host': "keyword-analysis.p.rapidapi.com",
    'x-rapidapi-key': "Your-X-RapidAPI-Key"
}

querystring = {"q": "john wick 3"}

response = requests.get(URL, headers=HEADERS, params=querystring).json()
print(response)

for item in response:
    name = item["name"]
    score = item["score"]

    print("name: {}, score: {}.".format(name, score))
```



[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

