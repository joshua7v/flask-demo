import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xcd\xd8X\x016q\xa5\xe4z\xa2\xcb\xcdo\xed\xd6\x19\x9f&\x9a$n*\xe7.'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False