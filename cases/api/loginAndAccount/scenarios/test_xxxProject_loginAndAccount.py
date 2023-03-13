from common.hamcrest.hamcrest import assert_that
from cases.api.loginAndAccount.api.test_xxxProject_login import Login
from cases.api.loginAndAccount.api.test_xxxProject_account import Account

class TestLoginAndAccount:

    def setup_class(self):
        self._api_login_client=Login()
        self._api_accpount_client=Account()
        # self._login_path='/public/authentication/login'

    def test_post_index(self):
        # step1: login and acquire token
        self._api_login_client.setup_class()
        httpResponse=self._api_login_client.post_index()
        print("\n===scenarios test of login response===\n")
        print(httpResponse.body)
        print("\n======================================\n")
        assert_that(200).is_equal_to(httpResponse.status_code)

        # step2: use token of step1 to call account api
        # httpResponse=self._api_accpount_client.test_post_index
