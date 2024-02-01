import getLocation
import requests
import io
from PIL import Image


def GetImage(url,x,y):
    #ピン画像を取得
    img_pin = Image.open('./pin2.png')
    
    #画像urlから画像を取得
    img_map = imread_web(url)

    x = y / 100
    y = x / 100
    
    center_x = img_map.height / 2
    center_y = img_map.width / 2
    print(center_x)
    print(center_y)
    
    #ブレンド
    img_map.paste(img_pin,(int(center_x +x) ,int(center_y + y)),img_pin)


    return img_map

def geturl():    
    mapdata = getLocation.getLocations()
    _url = mapdata.PoisImage
    return _url

def imread_web(url):
    # マップ画像を取得
    img = Image.open(io.BytesIO(requests.get(url).content))
    return img

# _url = geturl()
# img = GetImage(_url,0,0)
# img.show()


