import unittest
from app.models import GeneralNews, SourcesNews

genNews= GeneralNews

sourceNews = SourcesNews

class testSource(unittest.TestCase):
    '''
    Tests article test and source classes
    '''
    def setUp(self):
     
        self.newsBySource = genNews("HYPE BEAST","Tom Shelby","Rags to Riches",'2004-11-16',"This just shows its getting better","https://www.google.com","https://www.youttube.com")
        self.newsByArticle = sourceNews("hype", "Mo Money", "This just shows its getting better", "https://www.moringa.com", "EN", "Business")

    
    def test__init__(self):

        self.assertTrue(isinstance(self.newsBySource,genNews))
        self.assertTrue(isinstance(self.newsByArticle,sourceNews))

    def test_check_instance_variables_general(self):
        self.assertEquals(self.newsBySource.source,"HYPE BEAST")
        self.assertEquals(self.newsBySource.author,"Tom Shelby")
        self.assertEquals(self.newsBySource.title,"Rags to Riches")
        self.assertEquals(self.newsBySource.publishedAt,'2004-11-16')
        self.assertEquals(self.newsBySource.description,"This just shows its getting better")
        self.assertEquals(self.newsBySource.url,"https://www.google.com")
        self.assertEquals(self.newsBySource.urlToImage,"https://www.youttube.com")

    def test_check_instance_variables_source(self):
        self.assertEquals(self.newsByArticle.id,"hype")
        self.assertEquals(self.newsByArticle.name,"Mo Money")
        self.assertEquals(self.newsByArticle.description,"This just shows its getting better")
        self.assertEquals(self.newsByArticle.url,"https://www.moringa.com")
        self.assertEquals(self.newsByArticle.language,"EN")
        self.assertEquals(self.newsByArticle.category,"Business")
