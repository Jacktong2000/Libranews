from flask import Flask, render_template, request, jsonify
import json
import screenshot
import article_scrape
#import scrape
cnn_screenshot = screenshot.cnn_screenshot()
nbc_screenshot = screenshot.nbc_screenshot()
fox_screenshot = screenshot.fox_screenshot()
abc_screenshot = screenshot.abc_screenshot()
nydailynews_screenshot = screenshot.nydailynews_screenshot()
washingtonpost_screenshot = screenshot.washingtonpost_screenshot()
nytimes_screenshot = screenshot.nytimes_screenshot()

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    cnnimg1 = "static/screenshot/{}".format(cnn_screenshot[-1])
    nbcimg1 = "static/screenshot/{}".format(nbc_screenshot[-1])
    foximg1 = "static/screenshot/{}".format(fox_screenshot[-1])
    cnnimg2 = "static/screenshot/{}".format(cnn_screenshot[-4])
    nbcimg2 = "static/screenshot/{}".format(cnn_screenshot[-4])
    foximg2 = "static/screenshot/{}".format(cnn_screenshot[-4])

    if request.method == 'GET':
        return render_template('index.html',image1=cnnimg1, image2=nbcimg1,image3=foximg1,site1="http://cnn.com", site2="http://nbc.com", site3="http://foxnews.com")


@app.route("/grading", methods=['GET', 'POST'])
def grading():
    if request.method == 'GET':
        return render_template('grading.html', article='Search for an article')
    else:
        try:
            url = request.form['news_url']
            #sites = request.form['sites']
            #article = article_scrape.get_article(url,sites)
            #obj_score, sub_score = article_scrape.get_sentiment(article)
        except:
            error = 'Invalid URL'
            return render_template('grading.html', article=error)
        sites = request.form['sites']
        keyword = request.form['keyword']
        article = article_scrape.get_article(url,sites)
        obj_score, sub_score, key_score = article_scrape.get_sentiment(article, keyword)
        pos_neg = ''
        if obj_score >= 0:
            obj_pos = 'Positive'
        else:
            obj_score = obj_score * -1.0
            obj_pos = 'Negative'

        if sub_score >= 0:
            sub_pos = 'Positive'
        else:
            sub_score = sub_score * -1.0
            sub_pos = 'Negative'

        if key_score >= 0:
            key_pos = 'Positive'
        else:
            key_score = key_score * -1.0
            key_pos = 'Negative'

        return render_template('grading.html', article=article, objs='{} {}'.format(obj_pos, obj_score), \
                                subs='{} {}'.format(sub_pos, sub_score), keys='{} {}'.format(key_pos, key_score), \
                                obar=obj_score, sbar=sub_score, kbar=key_score)





@app.route("/process", methods=['POST'])
def homepage_process():
    box1 = request.form['box1']
    #box1 = request.args.get('box1', 0, type=str)
    cnnimg1 = "static/screenshot/{}".format(cnn_screenshot[-1])
    nbcimg1 = "static/screenshot/{}".format(nbc_screenshot[-1])
    foximg1 = "static/screenshot/{}".format(fox_screenshot[-1])
    abcimg1 = "static/screenshot/{}".format(abc_screenshot[-1])
    nytimesimg1 = "static/screenshot/{}".format(nytimes_screenshot[-1])
    washingtonpostimg1 = "static/screenshot/{}".format(washingtonpost_screenshot[-1])
    nydailynewsimg1 = "static/screenshot/{}".format(nydailynews_screenshot[-1])

    if str(box1) == 'cnn':
        img1=cnnimg1
        site1= "http://cnn.com/"
    elif str(box1) == 'nbc':
        img1=nbcimg1
        site1= "http://nbcnews.com/"
    elif str(box1) == 'fox':
        img1=foximg1
        site1= "http://foxnews.com/"
    elif str(box1) == 'nyt':
        img1=nytimesimg1
        site1= "http://nytimes.com/"
    elif str(box1) == 'wtp':
        img1=washingtonpostimg1
        site1= "http://washingtonpost.com/"
    elif str(box1) == 'abc':
        img1=abcimg1
        site1= "http://abcnews.go.com/"
    elif str(box1) == 'nyd':
        img1=nydailynewsimg1
        site1= "http://nydailynews.com/"

    #return jsonify(image1=img1,site1=site1)
    return jsonify({'image1':img1,'site1':site1})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
