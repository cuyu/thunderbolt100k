import requests
from thunderbolt100k import constants
import json
from thunderbolt100k.libs.compare_time import compare_time
from thunderbolt100k.libs.common import pl9k_color
import datetime

SESSION = requests.session()


def user_input():
    result = dict()
    result['WEATHER_TOKEN'] = raw_input("Please input your api key for https://api.apixu.com: ")
    result['WEATHER_CITY'] = raw_input('Please input the city of your location (e.g. Shanghai): ')
    return result


def fetch():
    assert 'WEATHER_TOKEN' in constants.CONFIG, 'You must set `THUNDERBOLT_WEATHER_TOKEN` in `~/.zshrc` file'
    assert 'WEATHER_CITY' in constants.CONFIG, 'You must set `THUNDERBOLT_WEATHER_CITY` in `~/.zshrc` file'
    response = SESSION.get(
        'https://api.apixu.com/v1/forecast.json?key={token}&q={city}&days=2'.format(
            token=constants.CONFIG.get('WEATHER_TOKEN'),
            city=constants.CONFIG.get('WEATHER_CITY')))

    return response.content if response.status_code == 200 else None


def display():
    path = constants.DATA_PATH_FORMAT.format('weather')
    with file(path, 'r') as f:
        content = json.load(f)
    now = datetime.datetime.now()
    # Use the next day's forecast info if the time is later than 23:00
    if now.hour >= 23:
        info = content['forecast']['forecastday'][1]['hour'][now.hour - 23]
    else:
        info = content['forecast']['forecastday'][0]['hour'][now.hour + 1]

    temp = info['temp_c']
    condition = info['condition']['text']
    update_time = content['current']['last_updated']
    delta_minute, delta_hour, delta_day = compare_time(update_time, '%Y-%m-%d %H:%M')

    if 'thunder' in condition or 'Thunder' in condition:
        symbol = "\uf0e7"
        symbol_color = pl9k_color(constants.CONFIG.get('WEATHER_THUNDER_COLOR'))
    elif 'rain' in condition or 'drizzle' in condition:
        symbol_color = pl9k_color(constants.CONFIG.get('WEATHER_RAIN_COLOR'))
        symbol = "\ue239"
    elif 'Cloudy' in condition:
        symbol = "\uf0c2"
        symbol_color = pl9k_color(constants.CONFIG.get('WEATHER_CLOUD_COLOR'))
    elif 'Overcast' in condition:
        symbol = "\uf0c2"
        symbol_color = pl9k_color(constants.CONFIG.get('WEATHER_OVERCAST_COLOR'))
    elif "Partly cloudy" in condition:
        symbol = "\ue21d"
        symbol_color = pl9k_color(constants.CONFIG.get('WEATHER_CLOUD_COLOR'))
    elif condition == 'Sunny' or condition == 'Clear':
        symbol = "\uf185"
        symbol_color = pl9k_color(constants.CONFIG.get('WEATHER_SUN_COLOR'))
    elif 'snow' in condition:
        symbol = "\uf2dc"
        symbol_color = pl9k_color(constants.CONFIG.get('WEATHER_SNOW_COLOR'))
    else:
        symbol_color = pl9k_color(constants.CONFIG.get('WEATHER_DEFAULT_COLOR'))
        symbol = "\uf422"

    if temp >= 35:
        temp_color = pl9k_color(constants.CONFIG.get('WEATHER_HIGH_TEMP_COLOR'))
        temp_symbol = '\uf2c7'
    elif temp >= 28:
        temp_color = pl9k_color(constants.CONFIG.get('WEATHER_MIDDLE_TEMP_COLOR'))
        temp_symbol = '\uf2c8'
    elif temp < 10:
        temp_color = pl9k_color(constants.CONFIG.get('WEATHER_LOW_TEMP_COLOR'))
        temp_symbol = '\uf2cb'
    else:
        temp_color = pl9k_color(constants.CONFIG.get('WEATHER_DEFAULT_COLOR'))
        temp_symbol = '\uf2c9'

    delay_minutes = delta_minute + 60 * delta_hour + 60 * 24 * delta_day

    if delta_day == 0:
        if delta_hour == 0:
            time_string = '>{0} min'.format(delta_minute)
        else:
            time_string = '>{0} hour'.format(delta_hour)
    else:
        time_string = '>{0} day'.format(delta_day)

    result = "%{" + symbol_color + "%}" + symbol + "  %{" + temp_color + "%}" + str(
        temp) + temp_symbol

    if delay_minutes >= int(constants.CONFIG.get('WEATHER_SHOW_UPDATE_TIME')):
        result += "%{" + pl9k_color(constants.CONFIG.get('WEATHER_UPDATE_TIME_COLOR')) + "%}" + "({0})".format(
            time_string)

    return result
