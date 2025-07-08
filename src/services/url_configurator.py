from config import URL_ADDRESS


class UrlConfigurator:
    def __init__(self, start_date: str, end_date: str):
        self.start_date = start_date
        self.end_date = end_date

    def get_configured_url(self) -> str:
        url_configured = URL_ADDRESS.format(self.start_date, self.end_date)
        return url_configured
