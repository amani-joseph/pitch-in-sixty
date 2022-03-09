import os


class Config:
    """
    General configurations parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://j03:j03@localhost/pitch' 
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST = 'app/static/photos'  
    #   email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587 
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'pitch'
    SENDER_EMAIL = 'pitch.in.sixxty@gmail.com'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kgxeopernurmpx:aa31071d97c85e5c57358ba27c61f3747494fcf1fd0737dbb3e851073e1210b5@ec2-44-194-167-63.compute-1.amazonaws.com:5432/dbhkq9mcmefecl'
    
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://j03:j03@localhost/pitch'
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://j03:j03@localhost/pitch'
    pass
    
class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://j03:j03@localhost/pitch'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}