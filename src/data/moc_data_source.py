import random

from data import DataSource


class MocDataSource(DataSource):

    @property
    def avocado_temp(self) -> float:
        return random.randint(-4, 30)

    @property
    def avocado_humid(self) -> float:
        return random.randint(3, 100)
