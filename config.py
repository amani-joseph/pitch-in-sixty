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
    """
    Production configuration child class
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")   

class TestConfig(Config):
#    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://j03:j03@localhost/pitch'
   SQLALCHEMY_DATABASE_URI = 'postgres://dqttppniumcfpe:10ef45779fd7d49ce8da89c0be6cfbd143788cff77ee04f7da6e5ede8c1507ea@ec2-34-231-183-74.compute-1.amazonaws.com:5432/d21ovpg5d76s9p'
    

class DevConfig(Config):
    """pitch-in-sixty
    Development config child class
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://j03:j03@localhost/pitch'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}