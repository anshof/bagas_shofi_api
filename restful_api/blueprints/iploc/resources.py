import requests,json, config
from math import cos, asin, sqrt, pi
from flask import Blueprint
from blueprints import app
from flask_restful import Api, reqparse, Resource

bp_iploc = Blueprint('iploc', __name__)
api = Api (bp_iploc)

class IpLocation(Resource):
    ip_host = app.config['IPLOC_HOST']
    token = app.config['TOKEN']
 

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ip', location='args', default=None)
        args = parser.parse_args()    
        

        response = requests.get(self.ip_host + '/' + args['ip'], params={'token':self.token})

        resp = response.json()
        point = resp['loc']
        mycity = resp['city']
        listloc = list(point.split(','))

        return {'latlon' : listloc, 
                'mycity' : mycity}

api.add_resource(IpLocation, '')


