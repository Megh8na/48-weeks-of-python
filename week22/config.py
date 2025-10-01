class Config:
    DEBUG = False
    TESTING = False
    LOG_LEVEL = 'INFO'

class DevelopmentConfig(Config):
    DEBUG = True
    LOG_LEVEL = 'DEBUG'

class ProductionConfig(Config):
    LOG_LEVEL = 'ERROR'

# Dictionary for app to load config
config_by_name = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
