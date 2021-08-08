from app import newsy
from .models import news_general, news_source
import urllib.request,json
from instance import config
from .config import Config

General = news_general.GeneralNews
Category = news_source.SourcesNews

api_key = config.NEWS_API_KEY

generalURL = Config.NEWS_API_GENERAL
categoryURL = Config.NEWS_API_SOURCE

def getTheRequired(any_list):

    general_results = []

    for singlecontent in any_list:
        author = singlecontent.get('author')
        title = singlecontent.get('title')
        publishedAt = singlecontent.get('publishedAt')
        description = singlecontent.get('description')
        url = singlecontent.get('url')
        urlToImage = singlecontent.get('urlToImage')

        news_article = General (author, title, publishedAt, description, url, urlToImage)
        general_results.append(news_article)

    return general_results

def getTheRequiredForCategory(any_list):

    category_results = []

    for singlecontent in any_list:
        id = singlecontent.get('id')
        name = singlecontent.get('name')
        description = singlecontent.get('description')
        url = singlecontent.get('url')
        language = singlecontent.get('language')
        category = singlecontent.get('category')

        news_article = Category (id, name, description, url, language, category)
        category_results.append(news_article)

    return category_results

def hp_allcontent():
    allContentURL = generalURL.format(api_key)

    with urllib.request.urlopen(allContentURL) as url:
        allcontentRAW = url.read()
        allcontentJSON = json.loads(allcontentRAW)

        if allcontentJSON['articles']:
            allcontent_list = allcontentJSON['articles']
            showToUser = getTheRequired(allcontent_list)
    
    return showToUser

def categorycontent(searchedCategory):

    categoryContentURL = categoryURL.format(searchedCategory, api_key)

    with urllib.request.urlopen(categoryContentURL) as url:
        categoryContentRAW = url.read()
        categoryContentJSON = json.loads(categoryContentRAW)

        if categoryContentJSON['sources']:
            categoryContent_list = categoryContentJSON['sources']
            showResult = getTheRequiredForCategory(categoryContent_list)
    
    return showResult


