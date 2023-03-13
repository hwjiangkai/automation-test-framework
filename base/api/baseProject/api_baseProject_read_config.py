from pojo.api.baseProject.baseProjectConfig import BaseProjectConfig
import configparser as ConfigParser

class API_BaseProject_Read_Config(object):
    __instance=None
    __inited=None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance=object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__inited is None:
            self.config=self._readConfig('config/baseProject/api_baseProject.conf')
            self.__inited=True

    def _readConfig(self,configFile):
        config = ConfigParser.ConfigParser()
        config.read(configFile,encoding='utf-8')
        baseProjectConfig=BaseProjectConfig()
        baseProjectConfig.url=config.get('servers','url')
        baseProjectConfig.init=config.get('isInit','init')
        return baseProjectConfig