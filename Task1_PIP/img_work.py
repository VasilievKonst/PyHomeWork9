from PIL import Image as i
import time

def img_open(data):

    img = i.open(data)
    img.show()
    time.sleep(1)
    img.close()
