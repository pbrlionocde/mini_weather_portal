from flask import Flask, render_template, request
#from app import app
import get_weather
import json
import datetime

app = Flask(__name__)


def get_data():
    with open ("static/json/city_name.json") as file:
        return json.load(file)

@app.route('/', methods=['GET', 'POST'])
def first():
    return render_template('first.html', data = get_data())



@app.route('/city', methods=['GET', 'POST'])
def city():
    if request.method == 'POST':
        id_city = int(request.form.get('l'))
        data = get_data()
        for id in data:
            if id['id'] == id_city:
                weather = get_weather.get_weather_dict( id['text'])
                return render_template('first.html', data = data, weather = weather, temp = "{:.2f}".format(weather['main']['temp'] - 273.15), date = datetime.date.today())








if __name__ == "__main__":
	app.run()
