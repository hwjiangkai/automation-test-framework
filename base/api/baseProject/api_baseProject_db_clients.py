from base.api.baseProject.api_baseProject_read_config import API_BaseProject_Read_Config

class API_BaseProject_DB_Clients(object):
    __instance=None
    __inited=None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance=object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__inited is None:
            self._baseProjectConfig = API_BaseProject_Read_Config().config
            # self.mysqlclient=MysqlClient('host','port','username','password','dbname')
            # self.oracleclient = OracleClient('host', 'port', 'username', 'password', 'dbname')
            self.__inited=True
