import requests
from config.constants import URL_ADDRESS

from services import WeatherDayFactory


def get_data():
    res = requests.get(URL_ADDRESS)
    return res.json()


if __name__ == "__main__":
    weather_list = WeatherDayFactory(get_data())
    # print(weather_list.get_days())
    for day in weather_list.get_days():
        print(day)


