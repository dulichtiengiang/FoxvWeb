
class Config(object): 
    # Default
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