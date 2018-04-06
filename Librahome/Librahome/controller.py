from flask import Flask, render_template, request
import screenshot
#import scrape
cnn_screenshot = screenshot.cnn_screenshot()
nbc_screenshot = screenshot.nbc_screenshot()
fox_screenshot = screenshot.fox_screenshot()

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    cnnimgpath = "static/screenshot/{}".format(cnn_screenshot[-1])
    nbcimgpath = "static/screenshot/{}".format(nbc_screenshot[-1])
    foximgpath = "static/screenshot/{}".format(fox_screenshot[-1])
    if request.method == 'GET':
        return render_template('index.html',image1=cnnimgpath, image2=foximgpath ,image3=nbcimgpath)
    else:
        title = request.form['news_title']
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
