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
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ljzbnxfpwjzpkq:a30e6588c099679e78e0d603cd2bef7327d8c598e7e9b1e0e73f6f21f3bbfd93@ec2-3-230-238-86.compute-1.amazonaws.com:5432/d4ang2adf9qt6n'
    
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