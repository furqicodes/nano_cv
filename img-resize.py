
from PIL import Image
import os, sys

path = "YOUR_DIR"
dirs = os.listdir( path )


def resize():
    i = 0 
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((640,480), Image.ANTIALIAS)
            imResize.save('Image_'+str(i)+'.jpg', 'JPEG', quality=90)
            i=i+1
            print("done image " + str(i))

resize()
