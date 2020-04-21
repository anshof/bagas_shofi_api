import json, os, config
from functools import wraps
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_claims

app = Flask(__name__) 

jwt = JWTManager(app)

def internal_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if not claims['status']:
            return {'status': 'FORBIDDEN', 'message': 'Internal Only!'}, 403
        else:
            return fn(*args, **kwargs)
    return wrapper

flask_env = os.environ.get('FLASK_ENV', 'Production')
if flask_env == "Production":
    app.config.from_object(config.ProductionConfig)
elif flask_env == "Testing":
    app.config.from_object(config.TestingConfig)
else:
    app.config.from_object(config.DevelopmentConfig)

db =SQLAlchemy(app) 
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@app.after_request 
def after_request(response): 
    try:
        requestData = request.get_json()
    except Exception as e:
        requestData = request.args.to_dict()
    if response.status_code==200:
        app.logger.warning("REQUEST_LOG\t%s", json.dumps({
            'method': request.method,
            'code': response.status,
            'uri': request.full_path,
            'request': requestData, 
            'response': json.loads(response.data.decode('utf-8'))}))
    else:
        app.logger.warning("REQUEST_LOG\t%s", json.dumps({
            'method': request.method,
            'code': response.status,
            'uri': request.full_path,
            'request': requestData, 
            'response': json.loads(response.data.decode('utf-8'))}))
        
    return response

from blueprints.iploc.resources import bp_iploc
app.register_blueprint(bp_iploc, url_prefix='/iploc')

from blueprints.zomato.resources import bp_zomato
app.register_blueprint(bp_zomato, url_prefix='/zomato')

from blueprints.auth import bp_auth
app.register_blueprint(bp_auth, url_prefix='/auth')

from blueprints.user.resources import bp_user
app.register_blueprint(bp_user, url_prefix='/user')

from blueprints.client.resources import bp_client
app.register_blueprint(bp_client, url_prefix='/client')
db.create_all()