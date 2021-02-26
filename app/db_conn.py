
import sqlite3
import traceback
import sys


def insert_value(weather, temp, date ):
    try:
        sqlite_connection = sqlite3.connect('static/weather_db.db')
        cursor = sqlite_connection.cursor()
        params = (weather['sys']['country'], weather['name'], weather['visibility'],
        weather['wind']['speed'], temp, weather['weather'][0]['main'],
        weather['main']['pressure'], weather['main']['humidity'], date)
        count = cursor.execute("""INSERT INTO weather (Country, City, Visibility, Wind, Temperature, Clouds, Pressure, Humidity, Date)
                                VALUES  ( ?, ?, ?, ?, ?, ?, ?, ?, ?)""", params)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Исключение", error.args)
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()


def select_all():
    try:
        sqlite_connection = sqlite3.connect('static/weather_db.db')
        cursor = sqlite_connection.cursor()
        count = cursor.execute('SELECT * FROM weather')
        return list(count)
    except sqlite3.Error as error:
        print("Исключение", error.args)
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("close db")


def filter(response):
    try:
        sqlite_connection = sqlite3.connect('static/weather_db.db')
        cursor = sqlite_connection.cursor()
        count = cursor.execute("SELECT * FROM weather WHERE City LIKE '{}%'".format(response[0]))
        return list(count)
    except sqlite3.Error as error:
        print("Исключение", error.args)
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("close db")
