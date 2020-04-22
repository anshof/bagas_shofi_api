import json
from sqlalchemy.sql import func
from . import app, client, cache, create_token, init_database

class TestAuthrCrud():    
    def test_post_auth_refresh_token(self, client, init_database):
        token = create_token()
        res = client.post('/auth/refresh',
                        headers={'Authorization': 'Bearer ' + token},
                        # query_string={'client_key':"internal", 'client_secret':"super_secret_client"},
                        content_type='application/json')
        
        res_json = json.loads(res.data)
        assert res.status_code == 200