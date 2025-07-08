from models import WeatherDayProcessedModel
from utils import Convertor
from .weather_fabric_base import WeatherFabricBase


class WeatherDayProcessedFabric(WeatherFabricBase):
    """
    Класс-фабрика.
    Принимает список объектов WeatherDayUnprocessedModel, парсит его и формирует
    список объектов класса WeatherDayProcessedModel
    в атрибуте days.
    """

    def _parse_weather_data(self):
        days: list[WeatherDayProcessedModel] = []
        for day in self.weather_data:
            date = day.date
            wind_speed_10m_m_per_s = [Convertor.knots_to_mps(ws_10) for ws_10 in day.wind_speed_10m]
            wind_speed_80m_m_per_s = [Convertor.knots_to_mps(ws_80) for ws_80 in day.wind_speed_80m]
            temperature_2m_celsius = [Convertor.fahrenheit_to_celsius(t_2) for t_2 in day.temperature_2m]
            apparent_temperature_celsius = [Convertor.fahrenheit_to_celsius(at) for at in day.apparent_temperature]
            temperature_80m_celsius = [Convertor.fahrenheit_to_celsius(t_80) for t_80 in day.temperature_80m]
            temperature_120m_celsius = [Convertor.fahrenheit_to_celsius(t_120) for t_120 in day.temperature_120m]
            soil_temperature_0cm_celsius = [Convertor.fahrenheit_to_celsius(st_0) for st_0 in day.soil_temperature_0cm]
            soil_temperature_6cm_celsius = [Convertor.fahrenheit_to_celsius(st_6) for st_6 in day.soil_temperature_6cm]
            rain_mm = [Convertor.inches_to_mm(r) for r in day.rain]
            showers_mm = [Convertor.inches_to_mm(sh) for sh in day.showers]
            snowfall_mm = [Convertor.inches_to_mm(sn) for sn in day.snowfall]
            visibility_m = [Convertor.feet_to_meters(v) for v in day.visibility]
            relative_humidity_2m = day.relative_humidity_2m

            dew_point_2m_celsius = [Convertor.fahrenheit_to_celsius(dp) for dp in day.dew_point_2m]
            avg_temperature_2m_24h = Convertor.avg_24(temperature_2m_celsius)
            avg_relative_humidity_2m_24h = Convertor.avg_24(relative_humidity_2m)
            avg_dew_point_2m_24h = Convertor.avg_24(dew_point_2m_celsius)
            avg_apparent_temperature_24h = Convertor.avg_24(apparent_temperature_celsius)
            avg_temperature_80m_24h = Convertor.avg_24(temperature_80m_celsius)
            avg_temperature_120m_24h = Convertor.avg_24(temperature_120m_celsius)
            avg_wind_speed_10m_24h = Convertor.avg_24(wind_speed_10m_m_per_s)
            avg_wind_speed_80m_24h = Convertor.avg_24(wind_speed_80m_m_per_s)
            avg_visibility_24h = Convertor.avg_24(visibility_m)

            total_rain_24h = Convertor.total_24(rain_mm)
            total_showers_24h = Convertor.total_24(showers_mm)
            total_snowfall_24h = Convertor.total_24(snowfall_mm)

            daylight_hours = Convertor.seconds_to_hours(day.daylight_duration)
            sunset_iso = Convertor.unixtime_to_iso8601(day.sunset)
            sunrise_iso = Convertor.unixtime_to_iso8601(day.sunrise)

            avg_temperature_2m_daylight = Convertor.calculate_daytime(
                timestamps=day.time,
                sunrise=day.sunrise,
                sunset=day.sunset,
                values=temperature_2m_celsius
            )
            avg_relative_humidity_2m_daylight = Convertor.calculate_daytime(
                timestamps=day.time,
                sunrise=day.sunrise,
                sunset=day.sunset,
                values=relative_humidity_2m
            )
            avg_dew_point_2m_daylight = Convertor.calculate_daytime(
                timestamps=day.time,
                sunrise=day.sunrise,
                sunset=day.sunset,
                values=dew_point_2m_celsius
            )
            avg_apparent_temperature_daylight = Convertor.calculate_daytime(
                timestamps=day.time,
                sunrise=day.sunrise,
                sunset=day.sunset,
                values=apparent_temperature_celsius
            )
            avg_temperature_80m_daylight = Convertor.calculate_daytime(
                timestamps=day.time,
                sunrise=day.sunrise,
                sunset=day.sunset,
                values=temperature_80m_celsius
            )
            avg_temperature_120m_daylight = Convertor.calculate_daytime(
                timestamps=day.time,
                sunrise=day.sunrise,
                sunset=day.sunset,
                values=temperature_120m_celsius
            )
            avg_wind_speed_10m_daylight = Convertor.calculate_daytime(
                timestamps=day.time,
                sunrise=day.sunrise,
                sunset=day.sunset,
                values=wind_speed_10m_m_per_s
            )
            avg_wind_speed_80m_daylight = Convertor.calculate_daytime(
                timestamps=day.time,
                sunrise=day.sunrise,
                sunset=day.sunset,
                values=wind_speed_80m_m_per_s
            )
            avg_visibility_daylight = Convertor.calculate_daytime(
                timestamps=day.time,
                sunrise=day.sunrise,
                sunset=day.sunset,
                values=visibility_m
            )
            total_rain_daylight = Convertor.calculate_daytime(
                timestamps=day.time,
                sunrise=day.sunrise,
                sunset=day.sunset,
                values=rain_mm,
                is_cumulative=True
            )
            total_showers_daylight = Convertor.calculate_daytime(
                timestamps=day.time,
                sunrise=day.sunrise,
                sunset=day.sunset,
                values=showers_mm,
                is_cumulative=True
            )
            total_snowfall_daylight = Convertor.calculate_daytime(
                timestamps=day.time,
                sunrise=day.sunrise,
                sunset=day.sunset,
                values=snowfall_mm,
                is_cumulative=True
            )

            days.append(WeatherDayProcessedModel(
                date=date,
                wind_speed_10m_m_per_s=wind_speed_10m_m_per_s,
                wind_speed_80m_m_per_s=wind_speed_80m_m_per_s,
                temperature_2m_celsius=temperature_2m_celsius,
                apparent_temperature_celsius=apparent_temperature_celsius,
                temperature_80m_celsius=temperature_80m_celsius,
                temperature_120m_celsius=temperature_120m_celsius,
                soil_temperature_0cm_celsius=soil_temperature_0cm_celsius,
                soil_temperature_6cm_celsius=soil_temperature_6cm_celsius,
                rain_mm=rain_mm,
                showers_mm=showers_mm,
                snowfall_mm=snowfall_mm,
                visibility_m=visibility_m,
                relative_humidity_2m=relative_humidity_2m,
                dew_point_2m_celsius=dew_point_2m_celsius,
                avg_temperature_2m_24h=avg_temperature_2m_24h,
                avg_relative_humidity_2m_24h=avg_relative_humidity_2m_24h,
                avg_dew_point_2m_24h=avg_dew_point_2m_24h,
                avg_apparent_temperature_24h=avg_apparent_temperature_24h,
                avg_temperature_80m_24h=avg_temperature_80m_24h,
                avg_temperature_120m_24h=avg_temperature_120m_24h,
                avg_wind_speed_10m_24h=avg_wind_speed_10m_24h,
                avg_wind_speed_80m_24h=avg_wind_speed_80m_24h,
                avg_visibility_24h=avg_visibility_24h,
                total_rain_24h=total_rain_24h,
                total_showers_24h=total_showers_24h,
                total_snowfall_24h=total_snowfall_24h,
                daylight_hours=daylight_hours,
                sunset_iso=sunset_iso,
                sunrise_iso=sunrise_iso,
                avg_temperature_2m_daylight=avg_temperature_2m_daylight,
                avg_relative_humidity_2m_daylight=avg_relative_humidity_2m_daylight,
                avg_dew_point_2m_daylight=avg_dew_point_2m_daylight,
                avg_apparent_temperature_daylight=avg_apparent_temperature_daylight,
                avg_temperature_80m_daylight=avg_temperature_80m_daylight,
                avg_temperature_120m_daylight=avg_temperature_120m_daylight,
                avg_wind_speed_10m_daylight=avg_wind_speed_10m_daylight,
                avg_wind_speed_80m_daylight=avg_wind_speed_80m_daylight,
                avg_visibility_daylight=avg_visibility_daylight,
                total_rain_daylight=total_rain_daylight,
                total_showers_daylight=total_showers_daylight,
                total_snowfall_daylight=total_snowfall_daylight
            ))

        return days
