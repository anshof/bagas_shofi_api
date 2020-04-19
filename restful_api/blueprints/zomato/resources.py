import requests, json, config
from flask import Blueprint
from flask_restful import Api, reqparse, Resource
from flask_jwt_extended import jwt_required
from blueprints import app, iploc
from math import cos, asin, sqrt, pi
from blueprints.iploc.resources import IpLocation

bp_zomato = Blueprint('zomato', __name__)
api = Api(bp_zomato)

class ZomatoApi(Resource):
    zomato_host = app.config['ZO_HOST']


    # payload = {}
    headers = {
        'Accept': 'application/json',
        'user-key': app.config['USER_KEY']
    }

    def distance(self,lat1, lon1, lat2, lon2):
        p = pi/180
        a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
        return 12742 * asin(sqrt(a))

    # @jwt_required
    def get(self):
        IpLocation()
        hasil = IpLocation().get()
        lat_now = float(hasil['latlon'][0])
        lon_now = float(hasil['latlon'][1])
        city = hasil['mycity']
        parser = reqparse.RequestParser()
        # parser.add_argument('entity_id', type=int, location='args', default=None)
        parser.add_argument('entity_type', location='args', default='city')
        parser.add_argument('q', location='args', default=None)
        parser.add_argument('count', location='args', default=None)
        args = parser.parse_args()

        response_city = requests.get(self.zomato_host + '/cities', params={'q': city}, headers=self.headers)
        response_city = response_city.json()
        # print(response_city)
        # print('===============================')
        
        
        if len(response_city['location_suggestions']) == 0:
            return 'Kota tidak terdaftar'


        id_city = response_city['location_suggestions'][0]['id']
        response_search = requests.get(self.zomato_host + '/search', params={'entity_id': id_city, 'entity_type': args['entity_type'], 'count': args['count']}, headers=self.headers)

        restorans = response_search.json()
        restorans = restorans['restaurants']
        
        output = []
        for restoran in restorans:
            result = {}

            result['restaurant_name'] = restoran['restaurant']['name']
            result['alamat'] = restoran['restaurant']['location']['address']
            lat_restaurant = float(restoran['restaurant']['location']['latitude'])
            lon_restaurant = float(restoran['restaurant']['location']['longitude'])
        #     lat2 = float(lat)
        #     lon2 = float(lon)

            jarak = self.distance(lat_now, lon_now, lat_restaurant, lon_restaurant)
            result['Jarak'] = '%s km'%(jarak)
            output.append(result)
        
        # return '%s lat : %s, lon : %s => jarak : %f kilometer' % (restoran[i]['restaurant']['name'], lat, lon, jarak)
        return output
api.add_resource(ZomatoApi, '')


