class WeatherDayBase:

    """
    Базовый класс, содержащий repr и обязательство slots
    """
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "__slots__"):
            raise TypeError(f"Class {cls.__name__} must have __slots__")

    def __repr__(self):
        attributes = []
        for attr in self.__slots__:
            if hasattr(self, attr):
                attributes.append(f"{attr}={getattr(self, attr)}")
        return f"{self.__class__.__name__}({', '.join(attributes)})"

    def __str__(self) -> str:
        return self.__repr__()
