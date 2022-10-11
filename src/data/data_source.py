from abc import abstractmethod, ABC
from data import AvocadoDTO


class DataSource(ABC):

    @property
    @abstractmethod
    def avocado(self) -> AvocadoDTO:
        pass
