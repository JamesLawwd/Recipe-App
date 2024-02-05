from decouple import config
import os 
class Config:
    SECRET_Key = config('SECRET_kEY')

    SQLALCHEMY_TRACK_MODIFICATIONS=config('SQLALCHEMY_TRACK_MODIFICATION',cast=bool)

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URL=""    