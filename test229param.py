# API
# icanhazdadjoke.com can be used as an API for fetching a random joke, a specific joke, or searching for jokes in a variety of formats.

# Calling the API
# Authentication
# No authentication is required to use the icanhazdadjoke.com API. Enjoy :)

# API response format
# All API endpoints follow their respective browser URLs, but we adjust the response formatting to be more suited for an API based on the provided HTTP Accept header.

# Accepted Accept headers:

# text/html - HTML response (default response format)
# application/json - JSON response
# text/plain - Plain text response

#....
# Search for dad jokes
# GET https://icanhazdadjoke.com/search - search for dad jokes.

# This endpoint accepts the following optional query string parameters:

# page - which page of results to fetch (default: 1)
# limit - number of results to return per page (default: 20) (max: 30)
# term - search term to use (default: list all jokes) ## Very Important !!!

import requests
url = "https://icanhazdadjoke.com/search"

response = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": "cat", "limit": 1}
)

data = response.json()
print("***data: ",data)
print(type(data)) #list
print("-----------data['results']------------------")
print(data["results"])
print(type(data["results"])) #dict
print("=====joke=========")

print( [x["joke"] for x in data["results"]])
print("-----------------------")
print(type(data["results"]))
### list_of_dists = [{dicts_key_value_pairs}] => list_of_dicts[0] just make dicts_key_value_pairs
print(data["results"][0]["joke"])

