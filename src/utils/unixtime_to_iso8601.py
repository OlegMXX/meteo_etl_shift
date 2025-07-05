import datetime


def unixtime_to_iso8601(unix_time: int) -> str:
    """
    Переводит время из вормата Юникс-тайм в ISO 8601
    :param unix_time: int
    :return: str
    """
    return datetime.datetime.fromtimestamp(unix_time, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")