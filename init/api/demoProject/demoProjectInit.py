from base.api.baseProject.api_baseProject_read_config import API_BaseProject_Read_Config

class BaseProjectInit:
    def __init__(self):
        self._api_baseProject_read_config=API_BaseProject_Read_Config().config

    def init(self):
        if int(self._api_baseProject_read_config.init)==0:
            return
        #每次测试前先清除上次构造的数据
        self._deinit()
        #初始化必要的数据，如在数据库中构建多种类型的账号，
        pass

    def _deinit(self):
        #清楚构造的数据
        pass
