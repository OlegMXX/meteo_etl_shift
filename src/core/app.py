import asyncio
import requests
from typing import List, Dict

from services import WeatherDayUnprocessedFabric, WeatherDayProcessedFabric
from models import WeatherDayProcessedModel, WeatherDayUnprocessedModel
from database import WeatherDB, WeatherCsv


class WeatherApp:
    """
    Основной класс приложения
    """
    def __init__(self, url_address: str,):
        self.url_address = url_address
        self.data = self._get_processed_data()
        self.db = WeatherDB()

    def _get_api_data(self) -> Dict:
        response = requests.get(self.url_address)
        return response.json()

    def _get_unprocessed_data(self) -> List[WeatherDayUnprocessedModel]:
        weather_list = WeatherDayUnprocessedFabric(self._get_api_data()).get_days()
        return weather_list

    def _get_processed_data(self) -> List[WeatherDayProcessedModel]:
        try:
            processed_weather_list = WeatherDayProcessedFabric(self._get_unprocessed_data()).get_days()
            return processed_weather_list
        except TypeError as e:
            print("The earliest available date for data is 2025-05-01")

    async def init_db(self) -> None:
        await self.db.connect()
        await self.db.create_table()
        await self.db.close()

    async def insert_weather_data(self) -> None:
        await self.db.connect()
        await asyncio.gather(*[self.db.insert_weather_data(day_data) for day_data in self.data])
        await self.db.close()

    def get_csv(self):
        csv_writer = WeatherCsv()
        csv_writer.save_to_file(self.data)
