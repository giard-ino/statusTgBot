from data import DataSource


class Avocado:

    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    def __str__(self) -> str:
        return f"Temperatura: {self.data_source.avocado.temperature} \n" \
               f"Umidità: {self.data_source.avocado.humidity}"
