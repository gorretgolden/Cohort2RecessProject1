import os
class Config:
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   JWT_SECRET_KEY = "protected"
   

   @staticmethod
   def init_app(app):
       pass

class DevelopmentConfig(Config):
   DEBUG=True
   SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:''@localhost/cohort_2_recess'


class TestingConfig(Config):
   DEBUG = True
   TESTING = True
   SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URL")


config = {
   'development': DevelopmentConfig,
   'testing': TestingConfig,
   'default': DevelopmentConfig
   }