import requests
import json
from app import app
from WeatherHTML import *
from apikey import appid

@app.route('/')
@app.route('/index')

def index():

    send_url_g = 'http://freegeoip.net/json'
    r_g = requests.get(send_url_g)
    j_g = json.loads(r_g.text)
    lat = j_g['latitude']
    lon = j_g['longitude']

    send_url_w = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'.format(lat, lon, appid)
    r_w = requests.get(send_url_w)
    j_w = json.loads(r_w.text)
    weather = j_w['weather'][0]
    strMain = weather['main']
    strDescription = weather['description']
    strIcon = weather['icon']
    print(j_w['weather'])

    strIcon = '01d'
    strColor = getBackgroundColorFromIcon(strIcon)
    
    return one + style_one + strColor + style_two + two + strIcon + three + strMain + " with " + strDescription + four