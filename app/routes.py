import requests
import json
from app import app
from html import *

@app.route('/')
@app.route('/index')

def index():
    appid = 'c00636f4e12a151f9695c2ca582f9521'

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
    #return "<head><title>W E A T H E R</title></head><body><h1>Hello World!</h1><p>" + weather['main'] + ": " + weather['description'] + "</p></body>" 

    return one + strIcon + two + strMain + " with " + strDescription + three