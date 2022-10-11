from data import DataSource
from data import AvocadoDTO


class JsonDataSource(DataSource):

    @property
    def avocado(self) -> AvocadoDTO:
        return AvocadoDTO(24, 34)
