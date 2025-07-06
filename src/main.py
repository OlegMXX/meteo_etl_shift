import requests
from config.constants import URL_ADDRESS

from services import WeatherDayUnprocessedFactory, WeatherDayProcessedFactory


def get_data():
    res = requests.get(URL_ADDRESS)
    return res.json()


if __name__ == "__main__":
    weather_list = WeatherDayUnprocessedFactory(get_data()).get_days()

    for day in weather_list:
        print(day)

    processed_weather_list = WeatherDayProcessedFactory(weather_list)

    for day in processed_weather_list.get_days():
        print(day)
