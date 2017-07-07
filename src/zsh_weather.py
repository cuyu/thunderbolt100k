import requests
import constants

SESSION = requests.session()


def get_weather_info():
    assert 'WEATHER_TOKEN' in constants.CONFIG, 'You must set `THUNDERBOLT_WEATHER_TOKEN` in `~/.zshrc` file'
    assert 'WEATHER_CITY' in constants.CONFIG, 'You must set `THUNDERBOLT_WEATHER_CITY` in `~/.zshrc` file'
    response = SESSION.get(
        'https://api.apixu.com/v1/current.json?key={token}&q={city}'.format(token=constants.CONFIG.get('WEATHER_TOKEN'),
                                                                            city=constants.CONFIG.get('WEATHER_CITY')))
    result = response.json()
    weather = result['current']['condition']['text']
    temp = result['current']['temp_c']
    return weather, temp


if __name__ == '__main__':
    get_weather_info()
