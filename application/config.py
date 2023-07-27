import os
from application.database import db_con_string

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class LocalDevelopmentConfig(Config):
    DB_DIR = os.path.join(base_dir, "../database_dir")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(DB_DIR, "db.sqlite3")
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SECURITY_PASSWORD_HASH = "bcrypt"
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT')
    SECURITY_REGISTERABLE = True
    SECURITY_USERNAME_ENABLE = False
    SECURITY_USERNAME_REQUIRED = False
    SECURITY_USERNAME_MIN_LENGTH = 8
    SECURITY_USERNAME_MAX_LENGTH = 32
    SECURITY_CHANGEABLE = False
    SECURITY_SEND_REGISTER_EMAIL = False #default is true



class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://{user}:{password}@{host}:{port}/{db_name}".format(
        user=db_con_string['user'], 
        password=db_con_string['password'], 
        host=db_con_string['host'], 
        port=db_con_string['port'],
        db_name=db_con_string['db_name']
    )
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT')
    SECURITY_PASSWORD_HASH = "bcrypt"
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
