import json
from . import app, client, cache, create_token, init_database

class TestUserCrud():
    id_user = 0
    def test_user_list(self, client, init_database):
        token = create_token()
        res = client.get(
            '/user', 
            headers={'Authorization':'Bearer ' + token}, 
            content_type='application/json'
            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_user_id_invalid(self, client, init_database):
        token = create_token()
        res = client.get(
            '/user/100', 
            headers={'Authorization':'Bearer ' + token}, 
            content_type='application/json'
            )
        res_json = json.loads(res.data)
        assert res.status_code == 404

    def test_user_insert(self, client, init_database):
        token = create_token()

        data = {
            "name": "rom",
            "age": 23,
            "sex": "Male",
            "client_id": 1
        }

        res = client.post(
            '/user', 
            json = data,
            headers={'Authorization': 'Bearer ' + token},
            content_type='application/json'
            )
        res_json = json.loads(res.data)
        assert res.status_code == 200
        self.id_user = res_json['id']

    def test_user_get_id(self, client, init_database):
        token = create_token()
        res = client.get(
            '/user/1', 
            headers={'Authorization':'Bearer ' + token}, 
            content_type='application/json'
            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_user_put(self, client, init_database):
        token = create_token()

        data = {
            "name": "rol",
            "age": 23,
            "sex": "Female",
            "client_id": 1
        }

        res = client.put(
            '/user/1', 
            json = data,
            headers={'Authorization': 'Bearer ' + token},
            content_type='application/json'
            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_user_put_invalid(self, client, init_database):
        token = create_token()

        data = {
            "name": "rol",
            "age": 23,
            "sex": "Female",
            "client_id": 1
        }

        res = client.put(
            '/user/100', 
            json = data,
            headers={'Authorization': 'Bearer ' + token},
            content_type='application/json'
            )
        res_json = json.loads(res.data)
        assert res.status_code == 404

    def test_user_delete(self, client, init_database):
        token = create_token()
        res = client.delete(
            '/user/1', 
            headers={'Authorization':'Bearer ' + token}, 
            content_type='application/json'
            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_user_delete_invalid(self, client, init_database):
        token = create_token()
        res = client.delete(
            '/user/100', 
            headers={'Authorization':'Bearer ' + token}, 
            content_type='application/json'
            )
        res_json = json.loads(res.data)
        assert res.status_code == 404

    def test_get_filterby(self, client, init_database):
        token = create_token()
        res = client.get(
            '/user', 
            query_string={
                "sex": "female",
                "orderby": "age",
                "sort": "desc"
            },
            headers={'Authorization':'Bearer ' + token}
            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_get_filterby2(self, client, init_database):
        token = create_token()
        res = client.get(
            '/user', 
            query_string={
                "sex": "female",
                "orderby": "sex",
                "sort": "desc"
            },
            headers={'Authorization':'Bearer ' + token}
            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_get_filterby3(self, client, init_database):
        token = create_token()
        res = client.get(
            '/user', 
            query_string={
                "sex": "male",
                "orderby": "age",
                "sort": "asc"
            },
            headers={'Authorization':'Bearer ' + token}
            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_get_filterby4(self, client, init_database):
        token = create_token()
        res = client.get(
            '/user', 
            query_string={
                "sex": "male",
                "orderby": "sex",
                "sort": "asc"
            },
            headers={'Authorization':'Bearer ' + token}
            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

    
        