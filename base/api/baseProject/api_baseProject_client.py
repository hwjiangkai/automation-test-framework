from base.api.baseProject.api_baseProject_read_config import API_BaseProject_Read_Config
from base.api.baseProject.api_baseProject_db_clients import API_BaseProject_DB_Clients
from common.httpclient.doRequest import DoRequest

class API_BaseProject_Client(object):
    __instance=None
    __inited=None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance=object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__inited is None:
            self.baseProjectConfig=API_BaseProject_Read_Config().config
            self.baseProjectDBClients=API_BaseProject_DB_Clients()
            self.doRequest=DoRequest(self.baseProjectConfig.url)

            self.__inited=True
