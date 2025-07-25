from typing import List

from .weather_base import WeatherDayBase


class WeatherDayUnprocessedModel(WeatherDayBase):
    """
    Модель описывает RAW показатели погоды за 1 день.
    """
    __slots__ = [
        "date",
        "time",
        "temperature_2m",
        "relative_humidity_2m",
        "dew_point_2m",
        "apparent_temperature",
        "temperature_80m",
        "temperature_120m",
        "wind_speed_10m",
        "wind_speed_80m",
        "visibility",
        "rain",
        "showers",
        "snowfall",
        "soil_temperature_0cm",
        "soil_temperature_6cm",
        "sunrise",
        "sunset",
        "daylight_duration"
    ]

    def __init__(
        self,
        date: str,
        time: List[int],
        temperature_2m: List[float],
        relative_humidity_2m: List[int],
        dew_point_2m: List[float],
        apparent_temperature: List[float],
        temperature_80m: List[float],
        temperature_120m: List[float],
        wind_speed_10m: List[float],
        wind_speed_80m: List[float],
        visibility: List[float],
        rain: List[float],
        showers: List[float],
        snowfall: List[float],
        soil_temperature_0cm: List[float],
        soil_temperature_6cm: List[float],
        sunrise: int,
        sunset: int,
        daylight_duration: float
    ):
        self.date = date
        self.time = time
        self.temperature_2m = temperature_2m
        self.relative_humidity_2m = relative_humidity_2m
        self.dew_point_2m = dew_point_2m
        self.apparent_temperature = apparent_temperature
        self.temperature_80m = temperature_80m
        self.temperature_120m = temperature_120m
        self.wind_speed_10m = wind_speed_10m
        self.wind_speed_80m = wind_speed_80m
        self.visibility = visibility
        self.rain = rain
        self.showers = showers
        self.snowfall = snowfall
        self.soil_temperature_0cm = soil_temperature_0cm
        self.soil_temperature_6cm = soil_temperature_6cm
        self.sunrise = sunrise
        self.sunset = sunset
        self.daylight_duration = daylight_duration
