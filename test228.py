import requests
url = "https://icanhazdadjoke.com/"

# response = requests.get(url) #option1 html
# response = requests.get(url, headers={"Accept":"text/plain"}) #option2

# print(response.text)


response = requests.get(url, headers={"Accept": "application/json"})#option3
text1 = response.text
print(text1)
print(type(text1)) #str

print("---------------------")
data = response.json()
print(data)
print(type(data)) #dict
print("=========================")
print(data["joke"])
print(f"status: {data['status']}")