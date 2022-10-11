import random
from data import DataSource, AvocadoDTO


class MocDataSource(DataSource):

    @property
    def avocado(self) -> AvocadoDTO:
        return AvocadoDTO(random.randint(40, 80), random.randint(-25, 30))
