import json

import requests

r = requests.delete('http://127.0.0.1:8000/uzduotis/1')
print(json.loads(r.text))