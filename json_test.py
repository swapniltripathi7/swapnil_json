import requests
import json
import pprint

response = requests.get('https://api.github.com/')

if response.status_code == 200:
	print('Success!')
elif response.status_code == 400:
	print('Not Found.')

response.encoding = 'utf-8'
parsed = response.json()

#pp = pprint.PrettyPrinter(indent=4, width=20, compact=False)
#pp.pprint(parsed)
print(json.dumps(parsed, indent=4, sort_keys=True))