from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
import hashlib, uuid
from blueprints import internal_required
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required, get_jwt_claims

from ..client.model import Clients

bp_auth = Blueprint('auth', __name__)
api = Api(bp_auth)

class CreateTokenResource(Resource):
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('client_key', location='args', required=True)
        parser.add_argument('client_secret', location='args', required=True)
        
        args = parser.parse_args()
        
        qry_client = Clients.query.filter_by(client_key=args['client_key']).first()
        client_salt = qry_client.salt
        encode = hashlib.sha512(('%s%s' % (args['client_secret'], client_salt)).encode('utf-8')).hexdigest()
        
        if encode == qry_client.client_secret:
            qry_client = marshal(qry_client, Clients.jwt_claims_fields)
            # qry_client['identifier'] = "altabatch5"
            # qry_client = {
            #     'status': "True"
            # }
            token = create_access_token(identity=args['client_key'], user_claims=qry_client)
            return {'token': token}, 200        
            # return marshal(qry_client, Clients.response_fields), 200, {'Content-Type': 'application/json'}
        else:
            return {'status': 'UNAUTHORIZED', 'message':'invalid key or secret'}, 403

    # @jwt_required
    # def post(self):
    #     claims = get_jwt_claims()
    #     return {'claims': claims}, 200

class RefreshTokenResource(Resource):
    
    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        token = create_access_token(identity=current_user)
        return {'token': token}, 200
             
api.add_resource(CreateTokenResource, '')
api.add_resource(RefreshTokenResource, '/refresh')

# from flask import Blueprint
# from flask_restful import Api, Resource, reqparse, marshal
# from blueprints import internal_required
# from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
# from ..client.model import Clients #nyambungin ke db
# import hashlib

# bp_auth = Blueprint('auth', __name__)
# api = Api(bp_auth)

# class CreateTokenResource(Resource):

#     def get(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('client_key', location='args', required=True)
#         parser.add_argument('client_secret', location='args', required=True)
#         args = parser.parse_args()

#         qry = Clients.query.filter_by(client_key=args['client_key']).first()

#         #enkripsi

#         if qry is not None:
#             encoded = ('%s%s' % (args['client_secret'], qry.salt)).encode('utf-8')
#             hash_pass = hashlib.sha512(encoded).hexdigest()
#             if hash_pass==qry.client_secret:
#                 qry=marshal(qry, Clients.jwt_claims_fields)
#                 qry['identifier']='alta batch 5'
#                 qry['status']=False
#                 token=create_access_token(identity=args['client_key'], user_claims=qry)
#                 return {'token':token},200
#         else:
#             if args['client_key']=='internal' and args['client_secret']=='rahasia':
#                 qry={
#                     'identifier':'alta batch 5',
#                     'status':True
#                 }
#                 token = create_access_token(identity=args['client_key'], user_claims=qry)
#                 return {'token':token}, 200
#             else:
#                 return{'status':'UNAUTHORIZED', 'message':'invalid key or secret'}, 404

#         @jwt_required
#         def post(self):
#             claims = get_jwt_claims()
#             return {'claims':claims}, 200     

# class RefreshTokenresource(Resource):
#     @jwt_required
#     def post(self):
#         current_user=get_jwt_identity()
#         claims = get_jwt_claims()
#         token=create_access_token(identity=current_user, user_claims= claims)
#         return {'claims':claims,'token':token}, 200

# api.add_resource(RefreshTokenresource, '/refresh')
# api.add_resource(CreateTokenResource, '')