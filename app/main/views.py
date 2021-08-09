from flask import render_template, request, redirect, url_for
from . import main
from ..request import hp_allcontent, categorycontent, sourcecontent, topiccontent

@main.route('/')
def homepagecontent():
    topicSearch = request.args.get('topicSearch')
    loadedcontent = hp_allcontent()

    if topicSearch:
        return redirect(url_for('main.topicLookOut', searchedTopic = topicSearch))
    return render_template('homepage.html', all_news = loadedcontent)

@main.route('/category')
def sourcescontentbeginning():
    businessCategory = categorycontent('business')
    enterntainmentCategory = categorycontent('entertainment')
    generalCategory = categorycontent('general')

    searchedCategory = request.args.get('categorySearch')
    if searchedCategory:
        return redirect(url_for('main.sourcescontentaftersearch', categorySearch = searchedCategory))
    else:
        return render_template('sources.html', business = businessCategory, entertainment = enterntainmentCategory, general = generalCategory)

@main.route('/category/<categorySearch>')
def sourcescontentaftersearch(categorySearch):
    categoryDisplay = categorycontent(categorySearch)
    title = f'{ categorySearch.upper() } Articles'
    return render_template('sources-results.html', title = title, categoryNews = categoryDisplay)

@main.route('/topic/<searchedTopic>')
def topicLookOut(searchedTopic):
    searchTopicList = searchedTopic.split(" ")
    searchTopicFormat = "+".join(searchTopicList)
    topicResult = topiccontent(searchTopicFormat)
    intro = f'Results for { searchedTopic.upper() }'
    title = searchedTopic.upper()
    return render_template('topicsearch.html', title = title, introduction = intro, search = topicResult )

@main.route('/source/bbc')
def bbc():
    title = 'BBC News'
    clickedOutlet = sourcecontent('bbc-news')
    return render_template('newsoutlet.html', title = title, outlet = clickedOutlet)

@main.route('/source/business-insider')
def businessInsider():
    title = 'Business Insider'
    clickedOutlet = sourcecontent('business-insider')
    return render_template('newsoutlet.html', title = title, outlet = clickedOutlet)

@main.route('/source/bleacher-report')
def bleacherReport():
    title = 'Bleacher Report'
    clickedOutlet = sourcecontent('bleacher-report')
    return render_template('newsoutlet.html', title = title, outlet = clickedOutlet)

    