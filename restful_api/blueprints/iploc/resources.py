import requests,json
from math import cos, asin, sqrt, pi
from flask import Blueprint
from blueprints import app
from flask_restful import Api, reqparse, Resource

bp_iploc = Blueprint('iploc', __name__)
api = Api (bp_iploc)

class IpLocation(Resource):
    ip_host = 'https://ipinfo.io/118.97.144.82'

 

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('token', location='args', default=None)
        args = parser.parse_args()    
        

        response = requests.get(self.ip_host, params={'token':args['token']})

        resp = response.json()
        point = resp['loc']
        mycity = resp['city']
        listloc = list(point.split(','))

        return {'latlon' : listloc, 
                'mycity' : mycity}

api.add_resource(IpLocation, '')


