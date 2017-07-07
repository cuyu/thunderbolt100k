import requests
import constants
import json
from libs.compare_time import compare_time

SESSION = requests.session()


def get_weather_info():
    assert 'WEATHER_TOKEN' in constants.CONFIG, 'You must set `THUNDERBOLT_WEATHER_TOKEN` in `~/.zshrc` file'
    assert 'WEATHER_CITY' in constants.CONFIG, 'You must set `THUNDERBOLT_WEATHER_CITY` in `~/.zshrc` file'
    response = SESSION.get(
        'https://api.apixu.com/v1/current.json?key={token}&q={city}'.format(token=constants.CONFIG.get('WEATHER_TOKEN'),
                                                                            city=constants.CONFIG.get('WEATHER_CITY')))
    return response.content


def read_weather_info():
    path = constants.DATA_PATH_FORMAT.format('weather')
    with file(path, 'r') as f:
        info = json.load(f)
    temp = info['current']['temp_c']
    condition = info['current']['condition']['text']
    update_time = info['current']['last_updated']
    delta_time = compare_time(update_time, '%Y-%m-%d %H:%M')

    if condition == 'rain':
        symbol_color = '%F{blue}'
        symbol = "\uf043"
    elif condition == 'cloudy':
        symbol = "\uf0c2"
        symbol_color = '%F{white}'
    elif condition == 'Sunny':
        symbol = "\uf185"
        symbol_color = '%F{yellow}'
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
