import json
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]


def change_value(identifier, val, data):
    for d in data:
        if identifier == d['id'] and d['value'] == "":
            d['value'] = val
            return
        elif d.get('values') is not None:
            change_value(identifier, val, d['values'])

with open(file1) as f1, open(file2) as f2, open(file3, 'w') as f3:
    values = json.load(f1)['values']
    tests = json.load(f2)
    f3.write(f2.read())

for elem in values:
    ID = elem['id']
    value = elem['value']

    change_value(ID, value, tests['tests'])

with open(file3, 'w') as f:
    json.dump(tests, f, indent=4)
