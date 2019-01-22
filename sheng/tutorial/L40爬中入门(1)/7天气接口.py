import urllib.request
import json
url = 'http://t.weather.sojson.com/api/weather/city/101180101'

resp = urllib.request.urlopen(url)
if resp.code == 200:
    weather_json = resp.read().decode('utf-8')
    weather_data = json.loads(weather_json)
    data = weather_data['data']
    yesterday = data['yesterday']


    tody_humidity = data['shidu']
    tody_temperature = data['wendu']
    tody_quality = data['quality']
    tody_ganmao = data['ganmao']
    print(f'今日温度:{tody_temperature},湿度:{tody_humidity},质量:{tody_quality},感冒指数:{tody_ganmao}')

    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    yesterday_type = yesterday['type']
    yesterday_date = yesterday['date']
    week = yesterday['week']
    print(f'昨日日期:{yesterday_date,week},温度:最{yesterday_high}∽最{yesterday_low},天气:{yesterday_type}')

    forecast = data['forecast']
    for i in forecast:
        print(f"""
           日期：{i["ymd"],i["week"]},
           天气：{i["type"]}
           温度：最{i["high"]}∽最{i["low"]}
           """)
