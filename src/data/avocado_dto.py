class AvocadoDTO:

    def __init__(self, temperature, humidity):
        self.__temperature = temperature
        self.__humidity = humidity

    @property
    def temperature(self) -> float:
        return self.__temperature

    @property
    def humidity(self) -> float:
        return self.__humidity
