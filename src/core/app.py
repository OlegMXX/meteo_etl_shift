import asyncio

import requests
from typing import List, Dict

from services import WeatherDayUnprocessedFabric, WeatherDayProcessedFabric
from models import WeatherDayProcessedModel, WeatherDayUnprocessedModel
from database import WeatherDB

from config import URL_ADDRESS


class WeatherApp:
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
        processed_weather_list = WeatherDayProcessedFabric(self._get_unprocessed_data()).get_days()
        return processed_weather_list

    async def init_db(self) -> None:
        await self.db.connect()
        await self.db.create_table()
        await self.db.close()

    async def insert_weather_data(self) -> None:
        await self.db.connect()
        await asyncio.gather(*[self.db.insert_weather_data(day_data) for day_data in self.data])
        await self.db.close()


async def main():
    app = WeatherApp(URL_ADDRESS)
    await app.init_db()
    await app.insert_weather_data()


if __name__ == "__main__":
    asyncio.run(main())
