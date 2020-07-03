import requests
import json

with open('recipe.json') as f:
  recipe = f.read()


response = requests.post("https://api.edamam.com/api/nutrition-details?app_id=9aac9873&app_key=e373a02590c47a6e8e3859f57f9551c6"
			,data = recipe
			,headers={
			"Content-Type": "application/json"
			})

if response.status_code == 200:
	print('Success!')
elif response.status_code == 400:
	print('Not Found.')

response.encoding = 'utf-8'
parsed = response.json()

#pp = pprint.PrettyPrinter(indent=4, width=20, compact=False)
#pp.pprint(parsed)
print(json.dumps(parsed, indent=4, sort_keys=True))
