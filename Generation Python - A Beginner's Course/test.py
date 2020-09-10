"""
s = input()
a = s.find('h')
b = s.rfind('h')
print(s[:a+1] + s[b-1:a-1:-1] + s[b+1:])
"""

import json

with open("clients.json", encoding="utf8") as f:
    clients = json.load(f)

y = {"Имя": 'Олег',
     "должность": "Стажер",
     "опыт": "0 лет"
     }

clients.append(y)
clients = sorted(clients, key=lambda s: s['опыт'])

with open('/home/dasha/Documents/QA/18 block/clients_1.json', 'w') as f:
    json.dump(clients, f, ensure_ascii=False)
with open('/home/dasha/Documents/QA/18 block/clients_1.json') as f:
    print(f.read())
