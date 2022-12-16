import json
import os

my_dict = {
    'name': 'Carlos Paiva',
    'language': 'python',
    'similar': ['javascript', 'csharp', 'java'],
    'users': 10000
}

#reading items of the dict
for key, value in my_dict.items():
    print(key, value)

#coverting dic in json
json.dumps(my_dict)

#creating a json_file
with open("utils_file/datas.json", "w") as file:
    file.write(json.dumps(my_dict))

#reading a json_file
with open("utils_file/datas.json", "r") as file:
    text = file.read()
    data = json.loads(text)

print(data)
print(data['name'])

#copy a data from a file
source_file = 'utils_file/datas.json'
destiny_file = 'utils_file/json_data.txt'

#method 01
with open(source_file, 'r') as in_file:
    text = in_file.read()
    with open(destiny_file, 'w') as out_file:
        out_file.write(text)

#method 02
open(destiny_file, 'w').write(open(source_file, 'r').read())

#reading a json_file
with open(destiny_file, 'r') as file:
    text = file.read()
    json_data = json.loads(text)

print(json_data)