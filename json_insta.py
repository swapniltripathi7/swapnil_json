import requests
import json
import pprint

response = requests.get('https://www.instagram.com/explore/tags/pizza/?__a=1')

def eachRecursive(obj):
	if isinstance(obj,dict):
		for k, v in obj.items():
			if k == "display_url":
				print(v)
			elif k == "dimensions":
				print(v)
			elif k == "taken_at_timestamp":
				print(v)
			else:
				eachRecursive(v)
	elif isinstance(obj,list):
		for item in obj:
			eachRecursive(item) 

if response.status_code == 200:
	print('Success!')
elif response.status_code == 400:
	print('Not Found.')

response.encoding = 'utf-8'
parsed = response.json()

eachRecursive(parsed)

#pp = pprint.PrettyPrinter(indent=4, width=20, compact=False)
#pp.pprint(parsed)
#print(json.dumps(parsed, indent=4, sort_keys=True))
