import psycopg
from data import DataSource, AvocadoDTO


class PgsqlDataSource(DataSource):

    def __init__(self, server, dbname, user, password):
        self._server = server
        self._dbname = dbname
        self._user = user
        self._password = password

    @property
    def avocado(self) -> AvocadoDTO:
        return AvocadoDTO(self.last_sensor_data("temperature"), self.last_sensor_data("humidity"))

    def last_sensor_data(self, sensor: str) -> float:
        with psycopg.connect(server=self._server, dbname=self._dbname, user=self._user,
                             password=self._password) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM test where sensor = %(sensor)s", {sensor: sensor})
                return cur.fetchone()[0]
