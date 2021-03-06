from .models import GeneralNews, SourcesNews
import urllib.request,json

api_key = None
generalURL = None
categoryURL = None 
topicURL = None 
sourceURL = None 

def configure_request(app):
    global api_key, generalURL, categoryURL, topicURL,sourceURL
    api_key = app.config['NEWS_API_KEY']
    generalURL = app.config['NEWS_API_GENERAL']
    categoryURL = app.config['NEWS_API_SOURCE']
    topicURL = app.config['NEWS_API_SEARCH']
    sourceURL = app.config['NEWS_API_SOURCE_URL']

def getTheRequired(any_list):

    general_results = []

    for singlecontent in any_list:
        source = singlecontent.get('source')
        author = singlecontent.get('author')
        title = singlecontent.get('title')
        publishedAt = singlecontent.get('publishedAt')
        description = singlecontent.get('description')
        url = singlecontent.get('url')
        urlToImage = singlecontent.get('urlToImage')

        news_article = GeneralNews (source, author, title, publishedAt, description, url, urlToImage)
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

        news_article = SourcesNews (id, name, description, url, language, category)
        category_results.append(news_article)

    return category_results

def hp_allcontent():
    allContentURL = generalURL.format(api_key)

    with urllib.request.urlopen(allContentURL) as url:
        allcontentRAW = url.read()
        allcontentJSON = json.loads(allcontentRAW)

        if allcontentJSON['articles']:
            allcontent_list = allcontentJSON['articles']
            showAllToUser = getTheRequired(allcontent_list)
    
    return showAllToUser

def categorycontent(searchedCategory):

    categoryContentURL = categoryURL.format(searchedCategory, api_key)

    with urllib.request.urlopen(categoryContentURL) as url:
        categoryContentRAW = url.read()
        categoryContentJSON = json.loads(categoryContentRAW)

        if categoryContentJSON['sources']:
            categoryContent_list = categoryContentJSON['sources']
            showCategoryResult = getTheRequiredForCategory(categoryContent_list)
    
    return showCategoryResult

def topiccontent(searchedTopic):

    topicContentURL = topicURL.format(searchedTopic, api_key)

    with urllib.request.urlopen(topicContentURL) as url:
        topicContentRAW = url.read()
        topicContentJSON = json.loads(topicContentRAW)

        if topicContentJSON['articles']:
            topicContent_list = topicContentJSON['articles']
            showTopicResult = getTheRequired(topicContent_list)
    
    return showTopicResult

def sourcecontent(searchedSource):
    sourceContentURL = sourceURL.format(searchedSource, api_key)

    with urllib.request.urlopen(sourceContentURL) as url:
        sourceContentRAW = url.read()
        sourceContentJSON = json.loads(sourceContentRAW)

        if sourceContentJSON['articles']:
            sourceContent_list = sourceContentJSON['articles']
            showSourceResult = getTheRequired(sourceContent_list)
    
    return showSourceResult




