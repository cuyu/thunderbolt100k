import requests
import constants
import json
from libs.compare_time import compare_time
import datetime

SESSION = requests.session()


def get_weather_info():
    assert 'WEATHER_TOKEN' in constants.CONFIG, 'You must set `THUNDERBOLT_WEATHER_TOKEN` in `~/.zshrc` file'
    assert 'WEATHER_CITY' in constants.CONFIG, 'You must set `THUNDERBOLT_WEATHER_CITY` in `~/.zshrc` file'
    response = SESSION.get(
        'https://api.apixu.com/v1/forecast.json?key={token}&q={city}&days=2'.format(
            token=constants.CONFIG.get('WEATHER_TOKEN'),
            city=constants.CONFIG.get('WEATHER_CITY')))
    return response.content


def read_weather_info():
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
    delta_time = compare_time(update_time, '%Y-%m-%d %H:%M')

    if 'thunder' in condition:
        symbol = "\uf0e7"
        symbol_color = '%F{yellow}'
    elif 'rain' in condition:
        symbol_color = '%F{blue}'
        symbol = "\ue239"
    elif 'Cloudy' in condition:
        symbol = "\uf0c2"
        symbol_color = '%F{white}'
    elif 'Overcast' in condition:
        symbol = "\uf0c2"
        symbol_color = '%F{grey}'
    elif "Partly cloudy" in condition:
        symbol = "\e21d"
        symbol_color = '%F{white}'
    elif condition == 'Sunny':
        symbol = "\uf185"
        symbol_color = '%F{yellow}'
    elif 'snow' in condition:
        symbol = "\uf2dc"
        symbol_color = '%F{white}'
    else:
        symbol_color = "%F{green}"
        symbol = "\uf2c7"

    if temp >= 35:
        temp_color = '%F{red}'
        temp_symbol = '\uf2c7'
    elif temp >= 28:
        temp_color = '%F{yellow}'
        temp_symbol = '\uf2c8'
    elif temp < 10:
        temp_color = '%F{blue}'
        temp_symbol = '\uf2cb'
    else:
        temp_color = '%F{green}'
        temp_symbol = '\uf2c9'

    if 'm' in delta_time:
        time_color = '%F{green}'
    elif 'h' in delta_time:
        time_color = '%F{yellow}'
    else:
        time_color = '%F{red}'

    print "%{" + symbol_color + "%}" + symbol + "  %{" + temp_color + "%}" + str(
        temp) + temp_symbol + "%{" + time_color + "%}" + "({0})".format(delta_time)


if __name__ == '__main__':
    read_weather_info()
