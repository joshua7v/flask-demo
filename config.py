import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xcd\xd8X\x016q\xa5\xe4z\xa2\xcb\xcdo\xed\xd6\x19\x9f&\x9a$n*\xe7.'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False