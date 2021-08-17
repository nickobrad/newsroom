class GeneralNews:
    def __init__(self, source, author, title, publishedAt, description, url, urlToImage):
        self.source = source
        self.author = author
        self.title = title
        self.publishedAt = publishedAt
        self.description = description
        self.url = url
        self.urlToImage = urlToImage 

class SourcesNews:

    def __init__(self, id, name, description, url, language, category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.language = language
        self.category = category
