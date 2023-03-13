from common.hamcrest.hamcrest import assert_that
from base.api.baseProject.api_baseProject_client import API_BaseProject_Client

class Account:

    def setup_class(self):
        self._api_baseProject_client=API_BaseProject_Client()
        self._login_path='/api/acc/account'

    def get_index(self):
        print("todo")

    def post_index(self):
        print("todo")

