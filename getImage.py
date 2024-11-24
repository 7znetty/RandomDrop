import getLocation
import requests
import io
from PIL import Image
import os


def GetImage(url,x,y):
    #ピン画像を取得
    pin_path = '/pin.png'
    dirname = os.path.dirname(__file__)
    pin_path = dirname + pin_path
    #print("pin" + str(os.path.isfile(pin_path)) + "\n" + pin_path)
    img_pin = Image.open(pin_path)
    
    #画像urlから画像を取得
    img_map = imread_web(url)

#('プレザント・ピアッツァ x:-20804', ' y:-65764 z:112')
#'フェンシング・フィールド x:-34960', ' y:-15236 z:112')
#'ICE島 x:113173', ' y:-84175')


#C5S4
    # _x = y / 140 #- img_pin.width
    # _y = -x / 140 #- img_pin.height
    
# #C2Remix時に調整(2024.11月)
#     y = -84175
#     x = 113173
    _x = y / 65 #- img_pin.width
    _y = -x / 65 #- img_pin.height

    center_x = img_map.height / 2
    center_y = img_map.width / 2

    pin_center_x = img_pin.width / 3
    pin_center_y = img_pin.height

    #ブレンド
    img_map.paste(img_pin,(int(center_x +_x - pin_center_x) ,int(center_y + _y - pin_center_y)),img_pin)


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


