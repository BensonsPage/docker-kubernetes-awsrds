"""Flask configuration."""
from os import environ

class Config:
    """Base config. uses local database server."""
    SECRET_KEY='YOURSECRETKEY'
    FLASK_DEBUG = True
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    # SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')

class ProductionConfig(Config):
    """Uses production database server."""
    DB_SERVER = environ.get('DB_SERVER')
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get('PROD_DATABASE_URI')

class DevelopmentConfig(Config):
    # HOST = '127.0.0.1'
    # HOST = environ.get('HOST')
    # USER = environ.get('USER')
    # PASSWORD = environ.get('PASSWORD')
    # DATABASE = environ.get('DATABASE')
    PORT = 3306
    FLASK_DEBUG = True

class TestingConfig(Config):
    TESTING = True
    HOST = 'db'
    USER = 'root'
    PASSWORD = 'scrum*ndup'
    PORT = 3306
    DATABASE = 'scrumstandupdb'