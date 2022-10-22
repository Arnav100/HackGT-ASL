from PIL import Image
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

trainpath = ""
testpath = ""
testimgpath = ""


def resize(path):
    for item in os.listdir(path):
        print(path + item)
        im = Image.open(path + item)
        if im.mode != 'RGB':
            im = im.convert('RGB')
        im.save(path + item, quality=25)


resize(trainpath)
resize(testpath)

img = mpimg.imread(testimgpath)
imgplot = plt.imshow(img)
plt.show()
