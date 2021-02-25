import json


with open ("city.json") as file:
	data = json.load(file) 

list_data = []
for i in data:
	#print (i['name'])
	list_data.append({"id":i['id'], "text":i["name"]})



data = {"results":list_data}
with open("city_name.json", "w") as f:
	json.dump(list_data, f)
