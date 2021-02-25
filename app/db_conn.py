
import sqlite3
import traceback
import sys


def insert_value():
    try:
        sqlite_connection = sqlite3.connect('weather_db.db')
        cursor = sqlite_connection.cursor()

        sqlite_insert_query = """INSERT INTO weather
                              (Country, City, Visibility, Wind, Clouds, Pressure, Humidity, Date)
                                VALUES  ({}, {}, {}, {}, {}, {}, {}, {})""".format(
                                weather['sys']['country'], weather['name'], weather['visibility'],
                                weather['wind']['speed'], temp, weather['weather'][0]['main'],
                                weather['main']['pressure'], weather['main']['humidity'], date
                                )

        count = cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        print("Запись успешно вставлена ​​в таблицу sqlitedb_developers ", cursor.rowcount)
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
            print("Соединение с SQLite закрыто")
