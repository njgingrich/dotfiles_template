#!/bin/python

import urllib.request, json

city = "Potsdam,NY"
api_key = "d313d0191d2e85999be902e452d2281f"

weather = eval(str(urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}".format(city, api_key)).read())[2:-1])

info = weather["weather"][0]["description"].capitalize()
temp = int(float(weather["main"]["temp"]) - 272.15)

as_f = temp * 9 / 5 + 32;

print("%s, %i °F" % (info, as_f))
