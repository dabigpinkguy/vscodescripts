from pip._vendor import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon/snorlax")
responseAll = requests.get("https://pokeapi.co/api/v2/pokemon")
print(response.status_code)
data = response.json()
dataAll = responseAll.json()
name = data['name']
height = data['height']
weight = data['weight']

print("your pokemon's name is ",name)
print("the pokemon's is ", height, "cm's tall ")
print("and your poekmon weighs ",weight, "lbs")


