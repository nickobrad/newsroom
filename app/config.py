import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    NEWS_API_GENERAL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_SOURCE = 'https://newsapi.org/v2/top-headlines/sources?category={}&apiKey={}'
    NEWS_API_SEARCH = 'https://newsapi.org/v2/everything?q={}&apiKey={}'

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    DEBUG = True

config_options = {'development':DevConfig}