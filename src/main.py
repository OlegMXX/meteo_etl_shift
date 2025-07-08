import sys
from pathlib import Path
import asyncio

from core import WeatherApp
from services import UrlConfigurator
from utils import input_validator

sys.path.append(str(Path(__file__).parent))

if __name__ == "__main__":
    async def main():
        print("Starting Weather App")
        print("The earliest date for data tou can choose is 2025-05-01")
        date_from = input("Input start date (YYYY-MM-DD):")
        date_to = input("Input end date (YYYY-MM-DD):")
        if input_validator(date_from, date_to):
            want_csv = input("Would you like to save the csv file? (y/n): ")
            want_db_save = input("Would you like to save the database? (y/n): ")

            url_address = UrlConfigurator(date_from, date_to).get_configured_url()
            app = WeatherApp(url_address)

            if want_csv == "y":
                app.get_csv()
                print("Data saved in CSV file")

            if want_db_save == "y":
                await app.init_db()
                await app.insert_weather_data()
                print("Data saved in DB")

    asyncio.run(main())
