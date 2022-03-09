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
    SQLALCHEMY_DATABASE_URI = 'postgresql://cwybneiomrugfl:cd378ab9f71cd27cb49e8b0a23c949c5cbacf57b84e7af7c7108fe33bfbf841c@ec2-52-70-205-234.compute-1.amazonaws.com:5432/d3fpocs4p9ko5v'   

class TestConfig(Config):
#    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://j03:j03@localhost/pitch'
   SQLALCHEMY_DATABASE_URI = 'postgresql://cwybneiomrugfl:cd378ab9f71cd27cb49e8b0a23c949c5cbacf57b84e7af7c7108fe33bfbf841c@ec2-52-70-205-234.compute-1.amazonaws.com:5432/d3fpocs4p9ko5v'
    

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