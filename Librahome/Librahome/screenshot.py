import os

path = '/mnt/c/Users/TheOn/Documents/Libranews/Librahome/Librahome/static/screenshot'

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
