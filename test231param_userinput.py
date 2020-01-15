import requests
from random import choice
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
    choceresult = choice(result)
    print(choceresult) #random.choice(list_name)
    print("*********choice w/o id***************")
    print(choceresult['joke'])
    print("--- just print result--")
    print(result[0]['joke'])
    print(result[1])
    print(result[2])
    print("**--print each dictionaries in a list**--")
    for i in range(0, len(result)): #last not incl
        print(result[i]['joke'])
else:
    print(f"There is no Joke about {user_input}: ")
    
    
    