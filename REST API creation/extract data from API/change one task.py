import json

import requests

nauja_uzduotis = {
    "pavadinimas": "Išplauti grindis",
    "atlikta": False
}

r = requests.put('http://127.0.0.1:8000/uzduotis/2', json=nauja_uzduotis)
print(json.loads(r.text))