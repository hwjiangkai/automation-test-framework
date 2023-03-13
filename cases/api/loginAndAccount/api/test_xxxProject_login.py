from common.hamcrest.hamcrest import assert_that
from base.api.baseProject.api_baseProject_client import API_BaseProject_Client
import ujson

class Login:

    def setup_class(self):
        self._api_baseProject_client=API_BaseProject_Client()
        self._login_path='/public/authentication/login'
        self._headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer",
            "Host": "stu-center-test.wukongacademy.com",
            "Origin": "https://student-test.wukongedu.net",
            "platform": "web",
            "Referer": "https://student-test.wukongedu.net/",
        }

    # def test_get_index(self):
    #     httpResponse=self._api_baseProject_client.doRequest.get(self._login_path)
    #     assert_that(200).is_equal_to(httpResponse.status_code)

    def post_index(self):
        geolocation={}
        geolocation.update({'oauthType':"PHONE_PASSWORD"})
        geolocation.update({'phone':"+93 703141455"})
        geolocation.update({'password':"wukong123"})
        self._api_baseProject_client.doRequest.setHeaders(self._headers)
        httpResponse=self._api_baseProject_client.doRequest.post_with_form(self._login_path, params=ujson.dumps(geolocation))
        print("\n===xxx project login api response===\n")
        print(httpResponse.body)
        print("\n==============\n")
        return httpResponse

    # @pytest.mark.search_kw
    # def test_search_kw(self):
    #     params={'wd':'apitest'}
    #     httpResponse = self._api_baseProject_client.doRequest.get(self._login_path,params)
    #     assert_that(200).is_equal_to(httpResponse.status_code)
