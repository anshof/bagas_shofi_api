import configparser
from datetime import timedelta

cfg = configparser.ConfigParser()
cfg.read('config.cfg')

class Config():
    SQLALCHEMY_DATABASE_URI = '%s+%s://%s:%s@%s:%s/%s'%(
        cfg['database']['default_connection'],
        cfg['mysql']['driver'],
        cfg['mysql']['user'],
        cfg['mysql']['password'],
        cfg['mysql']['host'],
        cfg['mysql']['port'],
        cfg['mysql']['db']

    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = cfg['jwt']['secret_key']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    IPLOC_HOST = cfg['iploc']['host']
    TOKEN = cfg['iploc']['token']
    ZO_HOST = cfg['zomato']['z_host']
    USER_KEY = cfg['zomato']['user-key']    

class DevelopmentConfig(Config):
    APP_DEBUG = True
    DEBUG = True
    MAX_BYTES = 10000

class ProductionConfig(Config):
    APP_DEBUG = False
    DEBUG = False
    MAX_BYTES = 10000

class TestingConfig(Config):
    APP_DEBUG = False
    DEBUG = False
    MAX_BYTES = 10000
    APP_PORT = 9000
    SQLALCHEMY_DATABASE_URI = '%s+%s://%s:%s@%s:%s/%s_testing' % (
        cfg['database']['default_connection'],
        cfg['mysql']['driver'],
        cfg['mysql']['user'],
        cfg['mysql']['password'],
        cfg['mysql']['host'],
        cfg['mysql']['port'],
        cfg['mysql']['db']
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = cfg['jwt']['secret_key']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    IPLOC_HOST = cfg['iploc']['host']
    TOKEN = cfg['iploc']['token']
    ZO_HOST = cfg['zomato']['z_host']
    USER_KEY = cfg['zomato']['user-key'] 