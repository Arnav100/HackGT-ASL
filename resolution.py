from PIL import Image
import os
import sys

trainpath = ""
testpath = ""


def resize(path):
    for item in os.listdir(path):
        print(path + item)
        print("Hello")
        im = Image.open(path + item)
        if im.mode != 'RGB':
            im = im.convert('RGB')
        im.save(path + item, quality=25)


resize(trainpath)
resize(testpath)
