from flask import Flask, render_template, request
import filter
import db_conn
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
                db_conn.insert_value(weather = weather, temp = "{:.2f}".format(weather['main']['temp'] - 273.15), date = datetime.date.today())
                date = datetime.datetime.now()
                return render_template('first.html', data = data, weather = weather, temp = "{:.2f}".format(weather['main']['temp'] - 273.15), date = date.date())


@app.route('/sec', methods=['GET', 'POST'])
def all_weather():
    weather = db_conn.select_all()
    set_city = {i[2] for i in weather}
    return render_template('second.html', weather=weather, city=set_city)


@app.route('/filter', methods=['GET', 'POST'])
def all_weather_filter():
    if request.method == 'POST':
        weather = db_conn.select_all()
        response = [request.form.get("city"), request.form.get("year_from"), request.form.get("month_from"), request.form.get("day_from"),
                    request.form.get("year_to"), request.form.get("month_to"), request.form.get("day_to")]

    set_city = {i[2] for i in weather}
    weather = filter.filter_by(response)
    return render_template('second.html', weather=weather, city=set_city)







if __name__ == "__main__":
	app.run()
