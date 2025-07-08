import csv
from datetime import datetime
from typing import List

from models import WeatherDayProcessedModel


class WeatherCsv:
    def __init__(self):
        self.filename = '{}.csv'.format(datetime.now().strftime("%Y%m%d-%H%M%S"))

    def save_to_file(self, data: List[WeatherDayProcessedModel]):
        headers = [
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
        rows = [
            [
                day.avg_temperature_2m_24h,
                day.avg_relative_humidity_2m_24h,
                day.avg_dew_point_2m_24h,
                day.avg_apparent_temperature_24h,
                day.avg_temperature_80m_24h,
                day.avg_temperature_120m_24h,
                day.avg_wind_speed_10m_24h,
                day.avg_wind_speed_80m_24h,
                day.avg_visibility_24h,
                day.total_rain_24h,
                day.total_showers_24h,
                day.total_snowfall_24h,
                day.avg_temperature_2m_daylight,
                day.avg_relative_humidity_2m_daylight,
                day.avg_dew_point_2m_daylight,
                day.avg_apparent_temperature_daylight,
                day.avg_temperature_80m_daylight,
                day.avg_temperature_120m_daylight,
                day.avg_wind_speed_10m_daylight,
                day.avg_wind_speed_80m_daylight,
                day.avg_visibility_daylight,
                day.total_rain_daylight,
                day.total_showers_daylight,
                day.total_snowfall_daylight,
                day.wind_speed_10m_m_per_s,
                day.wind_speed_80m_m_per_s,
                day.temperature_2m_celsius,
                day.apparent_temperature_celsius,
                day.temperature_80m_celsius,
                day.temperature_120m_celsius,
                day.soil_temperature_0cm_celsius,
                day.soil_temperature_6cm_celsius,
                day.rain_mm,
                day.showers_mm,
                day.snowfall_mm,
                day.visibility_m,
                day.relative_humidity_2m,
                day.dew_point_2m_celsius,
                day.daylight_hours,
                day.sunset_iso,
                day.sunrise_iso
            ]
            for day in data
        ]
        with open(self.filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows)
