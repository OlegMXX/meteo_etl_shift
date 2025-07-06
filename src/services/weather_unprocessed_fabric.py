from typing import List

from models import WeatherDayUnprocessedModel
from utils import Convertor


class WeatherDayUnprocessedFactory:
    """
    Класс-фабрика.
    Принимает словарь с API-респонза, парсит его и формирует
    список объектов класса WeatherDayUnprocessedModel
    в атрибуте days.
    """
    def __init__(self, weather_data: dict):
        self.weather_data = weather_data
        self.days = self._parse_weather_data()

    def _parse_weather_data(self):
        days: list[WeatherDayUnprocessedModel] = []
        cnt24 = 0
        cnt_day = 0
        for day in self.weather_data["daily"]["time"]:
            date = Convertor.unixtime_to_iso8601(day)
            time = self.weather_data["hourly"]["time"][cnt24:cnt24+24]
            temperature_2m = self.weather_data["hourly"]["temperature_2m"][cnt24:cnt24+24]
            relative_humidity_2m = self.weather_data["hourly"]["relative_humidity_2m"][cnt24:cnt24+24]
            dew_point_2m = self.weather_data["hourly"]["dew_point_2m"][cnt24:cnt24+24]
            apparent_temperature = self.weather_data["hourly"]["apparent_temperature"][cnt24:cnt24+24]
            temperature_80m = self.weather_data["hourly"]["temperature_80m"][cnt24:cnt24+24]
            temperature_120m = self.weather_data["hourly"]["temperature_120m"][cnt24:cnt24+24]
            wind_speed_10m = self.weather_data["hourly"]["wind_speed_10m"][cnt24:cnt24+24]
            wind_speed_80m = self.weather_data["hourly"]["wind_speed_80m"][cnt24:cnt24+24]
            visibility = self.weather_data["hourly"]["visibility"][cnt24:cnt24+24]
            rain = self.weather_data["hourly"]["rain"][cnt24:cnt24+24]
            showers = self.weather_data["hourly"]["showers"][cnt24:cnt24+24]
            snowfall = self.weather_data["hourly"]["snowfall"][cnt24:cnt24+24]
            soil_temperature_0cm = self.weather_data["hourly"]["soil_temperature_0cm"][cnt24:cnt24+24]
            soil_temperature_6cm = self.weather_data["hourly"]["soil_temperature_6cm"][cnt24:cnt24+24]
            sunrise = self.weather_data["daily"]["sunrise"][cnt_day:cnt_day+1][0]
            sunset = self.weather_data["daily"]["sunset"][cnt_day:cnt_day+1][0]
            daylight_duration = self.weather_data["daily"]["daylight_duration"][cnt_day:cnt_day+1][0]

            days.append(WeatherDayUnprocessedModel(
                date=date,
                time=time,
                temperature_2m=temperature_2m,
                relative_humidity_2m=relative_humidity_2m,
                dew_point_2m=dew_point_2m,
                apparent_temperature=apparent_temperature,
                temperature_80m=temperature_80m,
                temperature_120m=temperature_120m,
                wind_speed_10m=wind_speed_10m,
                wind_speed_80m=wind_speed_80m,
                visibility=visibility,
                rain=rain,
                showers=showers,
                snowfall=snowfall,
                soil_temperature_0cm=soil_temperature_0cm,
                soil_temperature_6cm=soil_temperature_6cm,
                sunrise=sunrise,
                sunset=sunset,
                daylight_duration=daylight_duration,
            ))
            cnt24 += 24
            cnt_day += 1

        return days

    def get_days(self) -> List[WeatherDayUnprocessedModel]:
        """
        Возвращает список объектов из атрибута days
        """
        return self.days


