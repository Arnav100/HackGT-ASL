from PIL import Image
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

trainpath = "/Users/manvirchahal/Downloads/archive/asl_alphabet_train/asl_alphabet_train/"
testpath = ""
testimgpath = "/Users/manvirchahal/Downloads/archive/asl_alphabet_train/asl_alphabet_train/Z/Z999.jpg"


def resize(path):
    for letter_dir in os.listdir(path):
        if letter_dir != ".DS_Store":
            for item in os.listdir(path + letter_dir + "/"):
                if os.path.isfile(path + letter_dir + "/" + item):
                    print("Hello")
                    im = Image.open(path + letter_dir + "/" + item)
                    if im.mode != 'RGB':
                        im = im.convert('RGB')
                    im.save(path + letter_dir + "/" + item, quality=50)


resize(trainpath)
# resize(testpath)

img = mpimg.imread(testimgpath)
imgplot = plt.imshow(img)
plt.show()
