from util.DBUtils import DBUtils
from datasource.dto.ConfigDto import ConfigDto
import db
from datetime import datetime as dt

class ConfigurationService:

    TABLE_NAME = "Configuration"

    def __init__(self):
        self.connection = db.initDB()

    def _createTable(self):
        query = """
            CREATE TABLE IF NOT EXISTS
            {self.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL UNIQUE,
                temperature INTEGER NOT NULL,
                humidity INTEGER NOT NULL,
                pressure INTEGER NOT NULL,
                publish BOOLEAN NOT NULL,
                lastModified TEXT NOT NULL
            );
        """
        DBUtils.izvrsiIZapisi(self.connection, query)

    def insertOrUpdate(self, configDto: ConfigDto):
        configuration = self._ifConfigExists(configDto.type)
        if configuration is None:
            query = f"""
                INSERT INTO {self.TABLE_NAME}
                (type, temperature, humidity, pressure, publish, lastModified)
                VALUES 
                ('{configDto.type}', {configDto.temperature}, {configDto.humidity}, {configDto.pressure}, {configDto.publish}, '{str(dt.now().timestamp())}')
            
            """
        else:
            query = f"""
                UPDATE {self.TABLE_NAME}
                SET temperature={configDto.temperature}, humidity={configDto.humidity}, pressure={configDto.pressure}, publish={configDto.publish}, lastModified='{str(dt.now.timestamp())}'
                WHERE type='{configDto.type}';
            """
        DBUtils.izvrsiIZapisi(self.connection, query)

    def readConfiguration(self, type):
        config = self._ifConfigExists(type)
        if config is not None:
            configDto = ConfigDto.createFromEntity(config)
            return configDto
        else:
            return None


    def _ifConfigExists(self, type):
        query = f"SELECT * FROM {self.TABLE_NAME} WHERE type='{type}';"
        return DBUtils.dohvatiPodatke(self.connection, query, one=True)