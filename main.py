import requests
import json
import datetime
import telegram
import math


def get_weather_message(weather_json, mode):
    print(mode, json.dumps(weather_json, indent=4, ensure_ascii=False))
    if mode == 'current':
        historical_response = requests.get(api_historical_url)
        historical_json_response = json.loads(historical_response.text)
        now_temp = float(json_response['current']['temp'])
        yesterday_temp = float(historical_json_response['current']['temp'])
        diff = now_temp - yesterday_temp
        if diff > 0:
            up_down_suffix = '높아요'
        else:
            up_down_suffix = '낮아요'
        daily = json_response['daily'][0]
        daily_total = get_weather_message(daily, '')
        # dt = int(weather_json['dt'])
        # date = datetime.datetime.fromtimestamp(dt)
        # str_time = date.strftime('%Y년 %m월 %d일 %H시') + ' (현재)'
        temp = weather_json['temp']
        feels_like = weather_json['feels_like']
        humidity = weather_json['humidity']
        clouds = weather_json['clouds']
        wind_speed = weather_json['wind_speed']
        is_rain = 'rain' in weather_json
        rain_hour = '0'
        if is_rain:
            rain_hour = weather_json['rain']['1h']
        description = weather_json['weather'][0]['description']
        # f'============================\n' + \
        return \
            f'# 현재 {description}\n\n' + \
            f'온도 (체감) : {temp}℃  ({feels_like}℃ )\n' + \
            f'어제보다 {abs(round(diff, 2))}˚ {up_down_suffix}\n\n' + \
            daily_total + \
            f'습도 : {humidity}%\n' + \
            f'풍속 : {wind_speed}m/s\n' + \
            f'구름 : {clouds}%\n' + \
            f'현재 강수량 : {rain_hour}mm\n' + \
            f'============================'

    elif mode == 'daily':
        daily_dt = int(weather_json['dt'])
        daily_date = datetime.datetime.fromtimestamp(daily_dt)
        daily_str_time = daily_date.strftime('%m월 %d일 %H시')
        temp_max = weather_json['temp']['max']
        temp_min = weather_json['temp']['min']
        temp_morn = weather_json['temp']['morn']
        temp_day = weather_json['temp']['day']
        temp_eve = weather_json['temp']['eve']
        temp_night = weather_json['temp']['night']
        feels_like_morn = weather_json['feels_like']['morn']
        feels_like_day = weather_json['feels_like']['day']
        feels_like_eve = weather_json['feels_like']['eve']
        feels_like_night = weather_json['feels_like']['night']
        humidity = weather_json['humidity']
        wind_speed = weather_json['wind_speed']
        clouds = weather_json['clouds']
        pop = float(weather_json['pop']) * 100
        is_rain = pop > 0
        rain = '0'
        if is_rain:
            rain = weather_json['rain']
        description = weather_json['weather'][0]['description']
        return \
            f'\n# {daily_str_time} ({description})\n\n' + \
            f'최저 / 최고 : {temp_min}℃ / {temp_max}℃\n' + \
            f'아침 (체감) : {temp_morn}℃ ({feels_like_morn}℃)\n' + \
            f'낮 (체감) : {temp_day}℃ ({feels_like_day}℃)\n' + \
            f'저녁 (체감) : {temp_eve}℃ ({feels_like_eve}℃)\n' + \
            f'밤 (체감) : {temp_night}℃ ({feels_like_night}℃)\n' + \
            f'강수확률 : {pop}%\n' + \
            f'강수량 : {rain}mm\n' + \
            f'습도 : {humidity}%\n' + \
            f'풍속 : {wind_speed}m/s\n' + \
            f'구름 : {clouds}%\n' + \
            f'\n============================'

    elif mode == 'hourly':
        dt = int(weather_json['dt'])
        date = datetime.datetime.fromtimestamp(dt)
        str_time = date.strftime('%H시')
        temp = weather_json['temp']
        feels_like = weather_json['feels_like']
        humidity = weather_json['humidity']
        clouds = weather_json['clouds']
        wind_speed = weather_json['wind_speed']
        is_rain = 'rain' in weather_json
        rain_hour = '0'
        if is_rain:
            rain_hour = weather_json['rain']['1h']
        description = weather_json['weather'][0]['description']
        return \
            f'\n# {str_time} ({description})\n\n' + \
            f'온도 (체감) : {temp}℃  ({feels_like}℃ )\n' + \
            f'습도 : {humidity}%\n' + \
            f'풍속 : {wind_speed}m/s\n' + \
            f'구름 : {clouds}%\n' + \
            f'강수량 : {rain_hour}mm' + \
            f'\n============================'
    else:
        temp_max = weather_json['temp']['max']
        temp_min = weather_json['temp']['min']
        temp_morn = weather_json['temp']['morn']
        temp_day = weather_json['temp']['day']
        temp_eve = weather_json['temp']['eve']
        temp_night = weather_json['temp']['night']
        feels_like_morn = weather_json['feels_like']['morn']
        feels_like_day = weather_json['feels_like']['day']
        feels_like_eve = weather_json['feels_like']['eve']
        feels_like_night = weather_json['feels_like']['night']
        pop = float(weather_json['pop']) * 100
        is_rain = pop > 0
        rain = '0'
        if is_rain:
            rain = weather_json['rain']
        description = weather_json['weather'][0]['description']
        return \
            f'{description} 예상\n' + \
            f'최저 / 최고 : {temp_min}℃ / {temp_max}℃\n' + \
            f'아침 (체감) : {temp_morn}℃ ({feels_like_morn}℃)\n' + \
            f'낮 (체감) : {temp_day}℃ ({feels_like_day}℃)\n' + \
            f'저녁 (체감) : {temp_eve}℃ ({feels_like_eve}℃)\n' + \
            f'밤 (체감) : {temp_night}℃ ({feels_like_night}℃)\n' + \
            f'강수확률 : {pop}%\n' + \
            f'예상 강수량 : {rain}mm\n'



api_key = 'OpenWeatherMapAPIKey'
api_city = 'Seoul'
api_lang = 'kr'
api_zip = '21399,kr'
# metric : Celsius
# imperial : Fahrenheit
api_units = 'metric'
# api_url = 'http://api.openweathermap.org/data/2.5/weather?q='+api_city+'&lang='+api_lang+'&units='+api_units+'&appid='+api_key
# api_url = 'http://api.openweathermap.org/data/2.5/weather?zip='+api_zip+'&appid='+api_key

guro_lat = '37.485385187270985'
guro_lon = '126.90141558277708'
guro_exclude = 'minutely'
historical_exclude = 'minutely,hourly'
now = datetime.datetime.now()
yesterday = now - datetime.timedelta(days=1)
now_millis = math.floor(yesterday.timestamp())

print('=================================================================================')
now_dt = int(now.timestamp())
now_date = datetime.datetime.fromtimestamp(now_dt)
now_str_time = now_date.strftime('%Y년 %m월 %d일')
print(now_str_time + ' start.')

api_one_call_url = f'https://api.openweathermap.org/data/2.5/onecall?lat={guro_lat}&lon={guro_lon}&lang={api_lang}&units={api_units}&exclude={guro_exclude}&appid={api_key}'
api_historical_url = f'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={guro_lat}&lon={guro_lon}&lang={api_lang}&units={api_units}&exclude={historical_exclude}&dt={now_millis}&appid={api_key}'

response = requests.get(api_one_call_url)
json_response = json.loads(response.text)
current_message = get_weather_message(json_response['current'], 'current')

daily_list = json_response['daily']
daily_message = ''
for daily_index in range(1, len(daily_list)):
    daily_weather = daily_list[daily_index]
    daily_message += '\n' + get_weather_message(daily_weather, 'daily')

hourly_list = json_response['hourly']
target_hour_index = [1, 2, 3, 5, 7, 9]
hourly_message = ''
for index in target_hour_index:
    hourly_weather = hourly_list[index]
    hourly_message += '\n' + get_weather_message(hourly_weather, 'hourly')


my_token = '텔레그램봇키'

bot = telegram.Bot(token=my_token)

prefix = f'## {now_str_time} 날씨 정보입니다.\n\n\n'

weather_message = prefix + '\n' + current_message + '\n' + hourly_message + '\n' + daily_message

now_log_time = now_date.strftime('[%Y-%m-%d %H:%M:%S]')

for update in bot.getUpdates():
    if update.message is None:
        continue
    chat_id_item = update.message.chat_id
    try:
        bot.sendMessage(chat_id=chat_id_item, text=weather_message)
        firstname = update.message.chat.first_name
        lastname = update.message.chat.last_name
        print(f'{now_log_time} {firstname} {lastname} 에게 전송 완료.')
    except:
        print(update.message.chat.first_name + ' ' + update.message.chat.last_name + ' 에게 전송 실패.')

print(weather_message)

print('=================================================================================')
print('')
print('')

