class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "kjrfh53jn5hgv5309fd4fsf"

    DB_NAME = "production_db"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"

    UPLOAD = "/home/username/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = "development_db"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"

    UPLOAD = "/home/username/project/flask/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True

    DB_NAME = "development_db"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"

    UPLOAD = "/home/username/project/flask/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = False