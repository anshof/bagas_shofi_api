from unittest import mock
from unittest.mock import patch
from blueprints import app
import json
from . import app, client,cache, create_token,init_database
class TestIploc():
    def mocked_request_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data
        if len(args) > 0 :
            if args[0] == app.config['IPLOC_HOST'] + '/ip':
                return MockResponse({
    "ip": "114.5.218.223",
    "hostname": "114-5-218-223.resources.indosat.com",
    "city": "Jakarta",
    "region": "Jakarta",
    "country": "ID",
    "loc": "-6.2146,106.8451",
    "org": "AS4761 INDOSAT Internet Network Provider",
    "timezone": "Asia/Jakarta"
}, 200)
            else:
                return MockResponse(None,404)
    
    @mock.patch('requests.get', side_effect=mocked_request_get)
    def test_check_iploc(self, get_mock, client):
        # token = create_token()
        res = client.get(
            '/iploc',
            query_string={"ip": "114.5.218.223"}
            # headers={"Authorization": 'Bearer '+token}
        )
        res_json = json.loads(res.data)
        assert res.status_code ==200
