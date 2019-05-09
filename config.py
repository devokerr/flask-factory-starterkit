import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root_password@localhost/database_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
