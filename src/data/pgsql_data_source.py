import psycopg2
from data import DataSource, AvocadoDTO


class PgsqlDataSource(DataSource):

    def __init__(self,server,dbname,user,password):
        self.conn = psycopg2.connect(server=server,dbname=dbname,user=user,password=password)

    @property
    def avocado(self) -> AvocadoDTO:
        pass

        