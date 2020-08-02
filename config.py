class Config:
    DEBUG = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:987654321@localhost/admin'
    SECRET_KEY = "_J=&c<44?=FKec%5Y<QHU3EkRA)TumVKq'Xu2[Dd]<4/u?t8r<"


class DevConfig(Config):
    DEBUG = True
