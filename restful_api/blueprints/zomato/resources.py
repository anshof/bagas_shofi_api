import requests, json, config
from flask import Blueprint
from flask_restful import Api, reqparse, Resource
from flask_jwt_extended import jwt_required
from blueprints import app, iploc, internal_required
from math import cos, asin, sqrt, pi
from blueprints.iploc.resources import IpLocation
from operator import itemgetter

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

    @internal_required
    def get(self):
        IpLocation()
        hasil = IpLocation().get()
        # print(hasil)
        latlon = hasil['loc']
        list_loc = list(latlon.split(','))
        lat_now = float(list_loc[0])
        lon_now = float(list_loc[1])
        city = hasil['city']
        parser = reqparse.RequestParser()
        # parser.add_argument('entity_id', type=int, location='args', default=None)
        parser.add_argument('entity_type', location='args', default='city')
        parser.add_argument('q', location='args', default=None)
        parser.add_argument('count', location='args', default=None)
        args = parser.parse_args()

        response_city = requests.get(self.zomato_host + '/cities', params={'q': city}, headers=self.headers)
        response_city = response_city.json()
        print(response_city)
        # print('===============================')
        
        
        if len(response_city['location_suggestions']) == 0:
            return 'Kota tidak terdaftar'


        id_city = response_city['location_suggestions'][0]['id']
        response_search = requests.get(self.zomato_host + '/search', params={'entity_id': id_city, 'entity_type': args['entity_type'], 'q': args['q'], 'count': args['count']}, headers=self.headers)

        restorans = response_search.json()
        # print(restorans)
        restorans = restorans['restaurants']


        if len(restorans) == 0:
            return "Kata kunci tidak ada"
        
        output = []
        for restoran in restorans:
            result = {}
        

            result['restaurant_name'] = restoran['restaurant']['name']
            result['rating'] = restoran['restaurant']['user_rating']['aggregate_rating']
            result['comment']=restoran['restaurant']['user_rating']['rating_text']
            result['open_hour'] = restoran['restaurant']['timings']
            result['cuisines'] = restoran['restaurant']['cuisines']
            result['currency'] = restoran['restaurant']['currency']
            result['cost_average_2_person'] = restoran['restaurant']['average_cost_for_two']
            result['address'] = restoran['restaurant']['location']['address']
            lat_restaurant = float(restoran['restaurant']['location']['latitude'])
            lon_restaurant = float(restoran['restaurant']['location']['longitude'])
        


            jarak = self.distance(lat_now, lon_now, lat_restaurant, lon_restaurant)
            result['distance'] = '%s km'%(jarak)
            output.append(result)
            jauh = sorted(output, key=itemgetter('distance'))

        
       
        return jauh
api.add_resource(ZomatoApi, '')


