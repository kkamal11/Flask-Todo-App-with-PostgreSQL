import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
db = SQLAlchemy()

db_con_string = {
    'user':os.environ.get('DB_USER',"postgres"),
    'password':os.environ.get('DB_PASSWORD',"you_may_put_default_password_here"),
    'host':os.environ.get('DB_HOST',"localhost"),
    'port':os.environ.get('DB_PORT','5432'),
    'db_name':os.environ.get('DB_NAME',"flask_db")
}