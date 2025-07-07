from typing import List

from .weather_base import WeatherDayBase


class WeatherDayProcessedModel(WeatherDayBase):
    """
    Модель описывает итоговые показатели погоды за 1 день.
    """
    __slots__ = [
        "date",
        "avg_temperature_2m_24h",
        "avg_relative_humidity_2m_24h",
        "avg_dew_point_2m_24h",
        "avg_apparent_temperature_24h",
        "avg_temperature_80m_24h",
        "avg_temperature_120m_24h",
        "avg_wind_speed_10m_24h",
        "avg_wind_speed_80m_24h",
        "avg_visibility_24h",
        "total_rain_24h",
        "total_showers_24h",
        "total_snowfall_24h",
        "avg_temperature_2m_daylight",
        "avg_relative_humidity_2m_daylight",
        "avg_dew_point_2m_daylight",
        "avg_apparent_temperature_daylight",
        "avg_temperature_80m_daylight",
        "avg_temperature_120m_daylight",
        "avg_wind_speed_10m_daylight",
        "avg_wind_speed_80m_daylight",
        "avg_visibility_daylight",
        "total_rain_daylight",
        "total_showers_daylight",
        "total_snowfall_daylight",
        "wind_speed_10m_m_per_s",
        "wind_speed_80m_m_per_s",
        "temperature_2m_celsius",
        "apparent_temperature_celsius",
        "temperature_80m_celsius",
        "temperature_120m_celsius",
        "soil_temperature_0cm_celsius",
        "soil_temperature_6cm_celsius",
        "rain_mm",
        "showers_mm",
        "snowfall_mm",
        "visibility_m",
        "relative_humidity_2m",
        "dew_point_2m_celsius",
        "daylight_hours",
        "sunset_iso",
        "sunrise_iso"
    ]

    def __init__(
        self,
        date: str,
        avg_temperature_2m_24h: float,
        avg_relative_humidity_2m_24h: float,
        avg_dew_point_2m_24h: float,
        avg_apparent_temperature_24h: float,
        avg_temperature_80m_24h: float,
        avg_temperature_120m_24h: float,
        avg_wind_speed_10m_24h: float,
        avg_wind_speed_80m_24h: float,
        avg_visibility_24h: float,
        total_rain_24h: float,
        total_showers_24h: float,
        total_snowfall_24h: float,
        avg_temperature_2m_daylight: float,
        avg_relative_humidity_2m_daylight: float,
        avg_dew_point_2m_daylight: float,
        avg_apparent_temperature_daylight: float,
        avg_temperature_80m_daylight: float,
        avg_temperature_120m_daylight: float,
        avg_wind_speed_10m_daylight: float,
        avg_wind_speed_80m_daylight: float,
        avg_visibility_daylight: float,
        total_rain_daylight: float,
        total_showers_daylight: float,
        total_snowfall_daylight: float,
        wind_speed_10m_m_per_s:  List[float],
        wind_speed_80m_m_per_s: List[float],
        temperature_2m_celsius: List[float],
        apparent_temperature_celsius: List[float],
        temperature_80m_celsius: List[float],
        temperature_120m_celsius: List[float],
        soil_temperature_0cm_celsius: List[float],
        soil_temperature_6cm_celsius: List[float],
        rain_mm: List[float],
        showers_mm: List[float],
        snowfall_mm: List[float],
        visibility_m: List[float],
        dew_point_2m_celsius: List[float],
        relative_humidity_2m: List[int],
        daylight_hours: float,
        sunset_iso: str,
        sunrise_iso: str
    ):
        self.date = date
        self.avg_temperature_2m_24h = avg_temperature_2m_24h
        self.avg_relative_humidity_2m_24h = avg_relative_humidity_2m_24h
        self.avg_dew_point_2m_24h = avg_dew_point_2m_24h
        self.avg_apparent_temperature_24h = avg_apparent_temperature_24h
        self.avg_temperature_80m_24h = avg_temperature_80m_24h
        self.avg_temperature_120m_24h = avg_temperature_120m_24h
        self.avg_wind_speed_10m_24h = avg_wind_speed_10m_24h
        self.avg_wind_speed_80m_24h = avg_wind_speed_80m_24h
        self.avg_visibility_24h = avg_visibility_24h
        self.total_rain_24h = total_rain_24h
        self.total_showers_24h = total_showers_24h
        self.total_snowfall_24h = total_snowfall_24h
        self.avg_temperature_2m_daylight = avg_temperature_2m_daylight
        self.avg_relative_humidity_2m_daylight = avg_relative_humidity_2m_daylight
        self.avg_dew_point_2m_daylight = avg_dew_point_2m_daylight
        self.avg_apparent_temperature_daylight = avg_apparent_temperature_daylight
        self.avg_temperature_80m_daylight = avg_temperature_80m_daylight
        self.avg_temperature_120m_daylight = avg_temperature_120m_daylight
        self.avg_wind_speed_10m_daylight = avg_wind_speed_10m_daylight
        self.avg_wind_speed_80m_daylight = avg_wind_speed_80m_daylight
        self.avg_visibility_daylight = avg_visibility_daylight
        self.total_rain_daylight = total_rain_daylight
        self.total_showers_daylight = total_showers_daylight
        self.total_snowfall_daylight = total_snowfall_daylight
        self.wind_speed_10m_m_per_s = wind_speed_10m_m_per_s
        self.wind_speed_80m_m_per_s = wind_speed_80m_m_per_s
        self.temperature_2m_celsius = temperature_2m_celsius
        self.apparent_temperature_celsius = apparent_temperature_celsius
        self.temperature_80m_celsius = temperature_80m_celsius
        self.temperature_120m_celsius = temperature_120m_celsius
        self.soil_temperature_0cm_celsius = soil_temperature_0cm_celsius
        self.soil_temperature_6cm_celsius = soil_temperature_6cm_celsius
        self.rain_mm = rain_mm
        self.showers_mm = showers_mm
        self.snowfall_mm = snowfall_mm
        self.visibility_m = visibility_m
        self.dew_point_2m_celsius = dew_point_2m_celsius
        self.relative_humidity_2m = relative_humidity_2m
        self.daylight_hours = daylight_hours
        self.sunset_iso = sunset_iso
        self.sunrise_iso = sunrise_iso
