class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_GENERAL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    NEWS_API_SOURCE = 'https://newsapi.org/v2/top-headlines/sources?category={}&apiKey={}'
    # https://newsapi.org/v2/top-headlines/sources?category=businessapiKey=eaaf5f4dcffb435c935d12b7bd2428cc

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True