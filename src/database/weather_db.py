import asyncpg
from typing import Optional

from models import WeatherDayProcessedModel


class WeatherDB:
    def __init__(self):
        self.pool: Optional[asyncpg.pool.Pool] = None

    async def connect(self):
        """
        Создает пул соединений с базой данных
        """
        self.pool = await asyncpg.create_pool(
            user="user_olly",
            password="4j8CXN1t35+7m6vh0",
            database="PostgreSQL-6601",
            host="localhost",
            port=5432,
            min_size=5,
            max_size=20
        )

    async def create_table(self):
        """
        Создает таблицу weather_data если она не существует
        """
        async with self.pool.acquire() as conn:
            await conn.execute(
                """     
                CREATE TABLE IF NOT EXISTS weather_data (
                    avg_temperature_2m_24h DECIMAL(5,2),
                    avg_relative_humidity_2m_24h DECIMAL(5,2),
                    avg_dew_point_2m_24h DECIMAL(5,2),
                    avg_apparent_temperature_24h DECIMAL(5,2),
                    avg_temperature_80m_24h DECIMAL(5,2),
                    avg_temperature_120m_24h DECIMAL(5,2),
                    avg_wind_speed_10m_24h DECIMAL(5,2),
                    avg_wind_speed_80m_24h DECIMAL(5,2),
                    avg_visibility_24h DECIMAL(10,2),
                    total_rain_24h DECIMAL(5,2),
                    total_showers_24h DECIMAL(5,2),
                    total_snowfall_24h DECIMAL(5,2),
                    
                    avg_temperature_2m_daylight DECIMAL(5,2),
                    avg_relative_humidity_2m_daylight DECIMAL(5,2),
                    avg_dew_point_2m_daylight DECIMAL(5,2),
                    avg_apparent_temperature_daylight DECIMAL(5,2),
                    avg_temperature_80m_daylight DECIMAL(5,2),
                    avg_temperature_120m_daylight DECIMAL(5,2),
                    avg_wind_speed_10m_daylight DECIMAL(5,2),
                    avg_wind_speed_80m_daylight DECIMAL(5,2),
                    avg_visibility_daylight DECIMAL(10,2),
                    total_rain_daylight DECIMAL(5,2),
                    total_showers_daylight DECIMAL(5,2),
                    total_snowfall_daylight DECIMAL(5,2),
                    
                    wind_speed_10m_m_per_s DECIMAL(5,2)[],
                    wind_speed_80m_m_per_s DECIMAL(5,2)[],
                    temperature_2m_celsius DECIMAL(5,2)[],
                    apparent_temperature_celsius DECIMAL(5,2)[],
                    temperature_80m_celsius DECIMAL(5,2)[],
                    temperature_120m_celsius DECIMAL(5,2)[],
                    soil_temperature_0cm_celsius DECIMAL(5,2)[],
                    soil_temperature_6cm_celsius DECIMAL(5,2)[],
                    rain_mm DECIMAL(5,2)[],
                    showers_mm DECIMAL(5,2)[],
                    snowfall_mm DECIMAL(5,2)[],
                    visibility_m INTEGER[],
                    relative_humidity_2m INTEGER[],
                    dew_point_2m_celsius DECIMAL(5,2)[],
                    
                    daylight_hours DECIMAL(5,2),
                    sunset_iso VARCHAR,
                    sunrise_iso VARCHAR
                    
                );
                """)

    async def insert_weather_data(self, data: WeatherDayProcessedModel) -> None:
        """
        Добавляет запись о погоде, если запись существует, вноситься она не будет.
        """
        async with self.pool.acquire() as conn:
            result = await conn.fetch(
                """
                SELECT * FROM weather_data
                WHERE sunrise_iso = $1 OR sunset_iso = $2
                """,
                data.sunrise_iso,
                data.sunset_iso
            )
            if len(result) != 0:
                print("База данных уже содержит вносимую запись. Повторная запись предотвращена.")
            else:
                await conn.execute("""
                    INSERT INTO weather_data
                    (
                        avg_temperature_2m_24h,
                        avg_relative_humidity_2m_24h,
                        avg_dew_point_2m_24h,
                        avg_apparent_temperature_24h,
                        avg_temperature_80m_24h,
                        avg_temperature_120m_24h,
                        avg_wind_speed_10m_24h,
                        avg_wind_speed_80m_24h,
                        avg_visibility_24h ,
                        total_rain_24h,
                        total_showers_24h,
                        total_snowfall_24h,
                        
                        avg_temperature_2m_daylight,
                        avg_relative_humidity_2m_daylight,
                        avg_dew_point_2m_daylight,
                        avg_apparent_temperature_daylight,
                        avg_temperature_80m_daylight,
                        avg_temperature_120m_daylight,
                        avg_wind_speed_10m_daylight,
                        avg_wind_speed_80m_daylight,
                        avg_visibility_daylight ,
                        total_rain_daylight,
                        total_showers_daylight,
                        total_snowfall_daylight,
                        
                        wind_speed_10m_m_per_s,
                        wind_speed_80m_m_per_s,
                        temperature_2m_celsius,
                        apparent_temperature_celsius,
                        temperature_80m_celsius,
                        temperature_120m_celsius,
                        soil_temperature_0cm_celsius,
                        soil_temperature_6cm_celsius,
                        rain_mm,
                        showers_mm,
                        snowfall_mm,
                        visibility_m,
                        relative_humidity_2m,
                        dew_point_2m_celsius,
                        
                        daylight_hours,
                        sunset_iso,
                        sunrise_iso
                    )
                    VALUES (
                    $1, $2, $3, $4, $5, $6, $7, $8, $9, $10,
                    $11, $12, $13, $14, $15, $16, $17, $18, $19, $20,
                    $21, $22, $23, $24, $25, $26, $27, $28, $29, $30,
                    $31, $32, $33, $34, $35, $36, $37, $38, $39, $40,
                    $41
                    )
                    """,
                                   data.avg_temperature_2m_24h,
                                   data.avg_relative_humidity_2m_24h,
                                   data.avg_dew_point_2m_24h,
                                   data.avg_apparent_temperature_24h,
                                   data.avg_temperature_80m_24h,
                                   data.avg_temperature_120m_24h,
                                   data.avg_wind_speed_10m_24h,
                                   data.avg_wind_speed_80m_24h,
                                   data.avg_visibility_24h,
                                   data.total_rain_24h,
                                   data.total_showers_24h,
                                   data.total_snowfall_24h,

                                   data.avg_temperature_2m_daylight,
                                   data.avg_relative_humidity_2m_daylight,
                                   data.avg_dew_point_2m_daylight,
                                   data.avg_apparent_temperature_daylight,
                                   data.avg_temperature_80m_daylight,
                                   data.avg_temperature_120m_daylight,
                                   data.avg_wind_speed_10m_daylight,
                                   data.avg_wind_speed_80m_daylight,
                                   data.avg_visibility_daylight,
                                   data.total_rain_daylight,
                                   data.total_showers_daylight,
                                   data.total_snowfall_daylight,

                                   data.wind_speed_10m_m_per_s,
                                   data.wind_speed_80m_m_per_s,
                                   data.temperature_2m_celsius,
                                   data.apparent_temperature_celsius,
                                   data.temperature_80m_celsius,
                                   data.temperature_120m_celsius,
                                   data.soil_temperature_0cm_celsius,
                                   data.soil_temperature_6cm_celsius,
                                   data.rain_mm,
                                   data.showers_mm,
                                   data.snowfall_mm,
                                   data.visibility_m,
                                   data.relative_humidity_2m,
                                   data.dew_point_2m_celsius,

                                   data.daylight_hours,
                                   data.sunset_iso,
                                   data.sunrise_iso
                                   )

    async def close(self):
        """Закрывает пул соединений"""
        await self.pool.close()
