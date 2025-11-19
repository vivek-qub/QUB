import json

json_data = '''
{
  "name": "Alice",
  "age": 30,
  "address": {
    "city": "Kozhikode",
    "state": "Kerala",
    "country": "India"
  },
  "hobbies": ["reading", "coding", "travel"]
}
'''

data = json.loads(json_data)

name = data['name']
age = data['age']
city = data['address']['city']
hobbies = data['hobbies']

print("Name:", name)
print("Age:", age)
print("City:", city)
print("Hobbies:", hobbies)
