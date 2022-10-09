from abc import abstractmethod,ABC


class DataSource(ABC):

    @property
    @abstractmethod
    def avocado_temp(self) -> float:
        pass

    @property
    @abstractmethod
    def avocado_humid(self) -> float:
        pass

