import requests

user_input = input("What would like to search for ? ")
url = "https://icanhazdadjoke.com/search"

response = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term":user_input}
)

data = response.json()
print(data)


print("-----------data['results']------------------")
result = data['results'] #a list of dictionaries
print(f"**** result is {result}")
print(f"-response.json()['results'] type is {type(response.json()['results'])}")
num_jokes = len(result)
print(f"*** number of joke : {num_jokes}")
print("-------==========-----------")
if num_jokes == 1:
    print(f"There is {num_jokes} Joke about {user_input}: ")
    print(result[0]['joke'])

    
elif num_jokes > 1:
    print(f"There are {num_jokes} Jokes about {user_input}: ")
    print("*****************************")
    print(result[0]['id'])
    
else:
    print(f"There is no Joke about {user_input}: ")
    
    
    