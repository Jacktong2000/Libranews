from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize, sent_tokenize
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
#import spacy


def get_article(search_url, sites):
    url = search_url
    try:
        uClient = uReq(url)
    except:
        return 'Not a valid URL'
    page_html = uClient.read()
    uClient.close()
    page = soup(page_html, "html.parser")
    check = ''

    if sites == 'CNN':
        #CNN
        update=page.findAll("p", {"class":"zn-body__paragraph speakable"})
        rest = page.findAll("div", {"class":"zn-body__paragraph"})
        #print (update[0].text)
        for k in rest:
            check += k.text
        if check == '':
            try:
                layer = page.find("div", {"id":"storytext"})
                rest = layer.findAll("p")
                for k in rest:
                    check += k.text
            except:
                check = 'Article not found, please check the URL.'

    elif sites =='NBC':
        try:
            article = page.findAll("p")
            for i in article:
                check += i.text
        except:
            check = 'Article not found, please check the URL.'

    elif sites == 'FOX':
        try:
            layer = page.find("div", {"class":"article-body"})
            article = layer.findAll("p")
            for i in article:
                #if i.startswith("<p"):
                check += i.text
        except:
            check = 'Article not found, please check the URL.'

    elif sites == 'ABC':
        try:
            article = page.findAll("p")
            for i in article:
                check += i.text
        except:
            check = 'Article not found, please check the URL.'

    elif sites == 'CBS':
        try:
            article = page.findAll("p")
            for i in article:
                check += i.text
        except:
            check = 'Article not found, please check the URL.'

    elif sites == "NYT":
        try:
            article = page.findAll("p", {"class":"story-body-text story-content"})
            for i in article:
                check += i.text
        except:
            check = 'Article not found, please check the URL.'

    elif sites == 'NYDailyNews':
        try:
            article = page.article
            new = article.findAll("p")
            for i in new:
                check += i.text
        except:
            check = 'Article not found, please check the URL.'

    else:
        return 'Not a valid news site!'

    return check


def get_sentiment(text, key):
    object = []
    subject = []
    keylist = []
    keyword = key
    #nlp = spacy.load('en')
    content = """{0}""".format(text)
    content_sentiment = TextBlob(content)

    #For whole article
    #object_sentiment = round(((content_sentiment.sentiment.polarity) * 100.0), 2)
    #subject_sentiment = round(((content_sentiment.sentiment.subjectivity) * 100.0), 2)
    
    #tryout = nlp(content)
    #sentien = tryout.sents
    sentien = sent_tokenize(content)
    for i in sentien:
        uno = TextBlob(i)
        if (uno.sentiment.polarity <= 0.0001) or (uno.sentiment.polarity >= 0.0001):
            object.append(uno.sentiment.polarity)
        #object.append(total_object)
        if (uno.sentiment.subjectivity <= 0.0001 ) or (uno.sentiment.subjectivity >= 0.0001):
            subject.append(uno.sentiment.subjectivity)
        #subject.append(total_subject)
    if keyword != '':
        for x in sentien:
            if keyword.lower() in x.lower():
                dose = TextBlob(x)
                keylist.append(dose.sentiment.polarity)
        try:
            keyword_sentiment = round(((sum(keylist)/len(keylist)) * 100.0),2)
        except:
            keyword_sentiment = 0.0
    else:
        keyword_sentiment = 0.0
    
 

    the_object = (sum(object)) / (len(object))
    the_subject = (sum(subject)) / (len(subject))
    object_sentiment = round((the_object * 100),2)
    subject_sentiment = round((the_subject * 100),2)
    #classify = TextBlob(content, analyzer=NaiveBayesAnalyzer())
    #overall_level = classify.sentiment.classification
    return object_sentiment, subject_sentiment, keyword_sentiment

