import requests
import json
import pprint

#response = requests.get('https://api.edamam.com/api/food-database/v2/parser?ingr=red%20apple&app_id=&app_key=')
response = requests.get('https://api.edamam.com/search?q=chicken biryani&app_id=f53fff68&app_key=1e26dbff572a1cdac4c4f3f31257b8dd&from=0&to=1')

def eachRecursive(obj):
	if isinstance(obj,dict):
		for k, v in obj.items():
			#if k == "totalNutrients":
			#	print("Nutrients :", v)
			if k == "ingredients":
				print("Ingredients :",v)
			elif k == "ingredientLines":
				print("Recipe :",v)
			elif k == "image":
				print("image url :",v)
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

#print(parsed['hits'])

#pp = pprint.PrettyPrinter(indent=4, width=20, compact=False)
#pp.pprint(parsed)
#print(json.dumps(parsed, indent=4, sort_keys=True))
