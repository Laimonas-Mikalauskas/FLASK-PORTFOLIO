r = requests.get('http://127.0.0.1:8000/uzduotis/2')
print(json.loads(r.text))