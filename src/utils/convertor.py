import datetime
from typing import List


class Convertor:
    """
    Класс с конверторами единиц
    """
    @staticmethod
    def unixtime_to_iso8601(unix_time: int) -> str:
        """
        Переводит время из вормата Юникс-тайм в ISO 8601
        :param unix_time: int
        :return: str
        """
        return datetime.datetime.fromtimestamp(unix_time, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """
        Переводит градусы по Фаренгейту в градусы Цельсия с округлением до второго знака

        C = (F - 32) * 5/9

        :param fahrenheit: float
        :return: float
        """
        return round((fahrenheit - 32) * 5 / 9, 2)


    @staticmethod
    def inches_to_mm(inches: float) -> float:
        """
        Переводит дюймы в сантиметры с округлением до второго знака

        1 дюйм = 25.4 мм

        :param inches: float
        :return: float
        """
        return round(inches * 25.4, 2)

    @staticmethod
    def knots_to_mps(knots: float) -> float:
        """
        Переводит узлы в метры в секунду

        1 узел = 0.514444 м/с

        :param knots: float
        :return: float
        """

        return round(knots * 0.514444, 2)

    @staticmethod
    def feet_to_meters(feet: float) -> float:
        """
        Переводит футы в метры c округлением до 2 знака

        1 фут = 0.3048 метра

        :param feet: float
        :return: float
        """
        return round(feet * 0.3048, 2)

    @staticmethod
    def avg_24(list_24: List[float | int]) -> float | int:
        """
        Находит среднее значение из списка
        :param list_24: List[float | int]
        :return: float | int
        """
        return round(sum(list_24) / len(list_24), 2)

    @staticmethod
    def total_24(list_24: List[float | int]) -> float | int:
        """
        Возвращает сумму всех элементов переданного списка
        :param list_24: list[float | int]
        :return: float | int
        """
        return round(sum(list_24), 2)

    @staticmethod
    def seconds_to_hours(seconds: float) -> float:
        """
        Переводит секунды в часы
        :param seconds: float:
        :return: float
        """
        return round(seconds / 3600, 2)

    @staticmethod
    def calculate_daytime(
            timestamps: List[int],
            sunrise: int,
            sunset: int,
            values: List[float | int],
            is_cumulative=False
    ):
        """
        Вычисляет среднеие дневные значения с учетом кумулятивности и
        особенности часового пояса, если в нем по unix-time закат
        может наступить раньше, чем рассвет

        :param timestamps: list[int] список unix timestamp текущих суток
        :param sunrise: int unix timestamp восход
        :param sunset: int unix timestamp закат
        :param values: list[int | float] почасовые значения вычисляемого параметра
        :param is_cumulative: bool является ли параметр кумулятивным
        :return: float сумма дневных значений, если is_cumulative=True.
        """

        total = 0.0
        total_weight = 0.0

        for i in range(len(timestamps)):
            current_time = timestamps[i]
            next_time = timestamps[i + 1] if i < len(
                timestamps) - 1 else current_time + 3600
            hour_duration = next_time - current_time

            if sunrise < sunset:
                start_day = max(current_time, sunrise)
                end_day = min(next_time, sunset)
                daylight_duration = max(0, end_day - start_day)
            else:
                start_day1 = max(current_time, sunrise)
                end_day1 = next_time
                duration1 = max(0, end_day1 - start_day1)

                start_day2 = current_time
                end_day2 = min(next_time, sunset)
                duration2 = max(0, end_day2 - start_day2)

                daylight_duration = duration1 + duration2

            weight = daylight_duration / hour_duration

            if is_cumulative:
                total += values[i] * weight
                total_weight += weight
            else:
                if daylight_duration > 0:
                    total += values[i]
                    total_weight += 1

        if total_weight == 0:
            return None

        if is_cumulative:
            return round(total, 2)
        else:
            return round(total / total_weight, 2)
