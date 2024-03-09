import json


data = {'number': 5,
        'string': 'hey',
        'boolean': True,
        'number_string': '12'}

string = json.dumps(data)
print(string)

new_data = json.loads(string)

print(type(new_data['number']))
print(type(new_data['string']))
print(type(new_data['boolean']))
print(type(new_data['number_string']))