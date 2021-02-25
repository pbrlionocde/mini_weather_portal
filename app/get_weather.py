import json, requests
import config_API

def get_weather_dict(city_name):
    return json.loads(requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name,config_API.API_KEY)).text)
