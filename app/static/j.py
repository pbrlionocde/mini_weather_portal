import json

import sqlite3
import traceback
import sys



with open ("city.json") as file:
	data = json.load(file) 

list_data = []
for i in data:
	#print (i['name'])
	list_data.append({"id":i['id'], "text":i["name"]})


for i in list_data:
	try:
		sqlite_connection = sqlite3.connect('weather_db.db')
		cursor = sqlite_connection.cursor()
		params = (i['id'], i['text'])
		count = cursor.execute("""INSERT INTO city (id, City)
								VALUES  ( ?, ?)""", params)
		sqlite_connection.commit()
		cursor.close()

	except sqlite3.Error as error:
		print("Не удалось вставить данные в таблицу sqlite")
		print("Класс исключения: ", error.__class__)
		print("Исключение", error.args)
		print("Печать подробноcтей исключения SQLite: ")
		exc_type, exc_value, exc_tb = sys.exc_info()
		print(traceback.format_exception(exc_type, exc_value, exc_tb))
	finally:
		if (sqlite_connection):
			sqlite_connection.close()