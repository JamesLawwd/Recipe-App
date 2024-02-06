from decouple import config
import os 
 
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_Key = config('SECRET_kEY')

    SQLALCHEMY_TRACK_MODIFICATIONS=config('SQLALCHEMY_TRACK_MODIFICATION',cast=bool)

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URL="sqlite:///"+os.path.join(BASE_DIR,'dev.db') 
    DEBUG=True
    SQLALCHEMY_ECHO=True

class ProdConfig(config):
    pass

class TestConfig(config):
    pass