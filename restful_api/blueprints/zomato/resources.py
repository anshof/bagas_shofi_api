import requests, json, config
from flask import Blueprint
from flask_restful import Api, reqparse, Resource
from flask_jwt_extended import jwt_required
from blueprints import app, iploc
from math import cos, asin, sqrt, pi

bp_zomato = Blueprint('zomato', __name__)
api = Api(bp_zomato)

class ZomatoApi(Resource):
    zomato_host = app.config['ZO_HOST']

    # payload = {}
    headers = {
        'Accept': 'application/json',
        'user-key': app.config['USER_KEY']
    }

    # def distance(lat1, lon1, lat2, lon2):
    #     p = pi/180
    #     a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    #     return 12742 * asin(sqrt(a))

    # @jwt_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('entity_id', type=int, location='args', default=None)
        parser.add_argument('entity_type', location='args', default=None)
        parser.add_argument('q', location='args', default=None)
        parser.add_argument('count', location='args', default=None)
        args = parser.parse_args()

        response = requests.get(self.zomato_host, params={'entity_id': args['entity_id'], 'entity_type': args['entity_type'], 'q': args['q'], 'count': args['count']}, headers=self.headers)

        restoran = response.json()
        # restoran = restoran['restaurants']
        
        # for i in range(len(restoran)):

        #     lat = restoran['i']['restaurant']['location']['latitude']
        #     lon = restoran['i']['restaurant']['location']['longitude']
            
        #     lat1 = float(iploc.resources.listloc[0])
        #     lon1 = float(iploc.resources.listloc[1])

        #     lat2 = float(lat)
        #     lon2 = float(lon)

        #     jarak = distance(lat1, lon1, lat2, lon2)
        
        # return '%s lat : %s, lon : %s => jarak : %f kilometer' % (restoran[i]['restaurant']['name'], lat, lon, jarak)
        return restoran


api.add_resource(ZomatoApi, '')


