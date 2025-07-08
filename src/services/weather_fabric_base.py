from typing import List, Union, Dict
from abc import ABC, abstractmethod

from models import WeatherDayUnprocessedModel, WeatherDayProcessedModel


class WeatherFabricBase(ABC):
    """
    Базовый класс для всех фабрик объектов погоды на день.
    """
    def __init__(self, weather_data: List[Union[WeatherDayUnprocessedModel, Dict]]):
        self.weather_data = weather_data
        self.days = self._parse_weather_data()

    @abstractmethod
    def _parse_weather_data(self):
        """
        Обязательство реализации функции для создания атрибута days
        :return:
        """
        pass

    def get_days(self) -> List[Union[WeatherDayUnprocessedModel, WeatherDayProcessedModel]]:
        """
        Возвращает список объектов из атрибута days
        """
        return self.days
