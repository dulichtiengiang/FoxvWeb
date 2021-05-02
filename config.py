
import os
class Config(object): 
    #Default
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    TESTING=False
    DEBUG=False
    SECRET_KEY = 'you-will-never-guess'

class Development(Config):
    DEBUG=True

class TESTING(Config):
    TESTING=True

config={
    'development': Development,
    'testing': TESTING
}