import os

path = './static/screenshot'

def cnn_screenshot():
    cnnscreenshot = [f for f in os.listdir(path) if f.endswith('CNN.png')]
    cnnscreenshot.sort()
    return cnnscreenshot

def nbc_screenshot():
    nbcscreenshot = [f for f in os.listdir(path) if f.endswith('NBC.png')]
    nbcscreenshot.sort()
    return nbcscreenshot

def fox_screenshot():
    foxscreenshot = [f for f in os.listdir(path) if f.endswith('FOX.png')]
    foxscreenshot.sort()
    return foxscreenshot

def abc_screenshot():
    abcscreenshot = [f for f in os.listdir(path) if f.endswith('ABC.png')]
    abcscreenshot.sort()
    return abcscreenshot

def washingtonpost_screenshot():
    washingtonpostscreenshot = [f for f in os.listdir(path) if f.endswith('WASHINGTONPOST.png')]
    washingtonpostscreenshot.sort()
    return washingtonpostscreenshot

def nytimes_screenshot():
    nytimesscreenshot = [f for f in os.listdir(path) if f.endswith('NEWYORKTIMES.png')]
    nytimesscreenshot.sort()
    return nytimesscreenshot

def nydailynews_screenshot():
    nydailynewsscreenshot = [f for f in os.listdir(path) if f.endswith('NYDAILYNEWS.png')]
    nydailynewsscreenshot.sort()
    return nydailynewsscreenshot

#print(nbc_screenshot())

