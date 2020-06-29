import requests
import json
import pprint

response = requests.get('https://api.edamam.com/search?q=chicken&app_id=f53fff68&app_key=1e26dbff572a1cdac4c4f3f31257b8dd&from=0&to=5')

if response.status_code == 200:
	print('Success!')
elif response.status_code == 400:
	print('Not Found.')

response.encoding = 'utf-8'
parsed = response.json()

#pp = pprint.PrettyPrinter(indent=4, width=20, compact=False)
#pp.pprint(parsed)
print(json.dumps(parsed, indent=4, sort_keys=True))
