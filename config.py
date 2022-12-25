class Config(object):
    DEBUG = False
    TESTING = False
    
class Development(Config):
    DEBUG = True
    ENV_VALUE = "Development"

class Testing(Config):
    TESTING = True
    DEBUG = True
    ENV_VALUE = "Testing"

class Production(Config):
    DEBUG = False
    ENV_VALUE = "Production"
    
