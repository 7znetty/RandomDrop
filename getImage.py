import cv2
import getLocation
import requests
import tempfile
import os

def GetImage(url,x,y):
    #ピン画像を取得
    img_pin = cv2.imread ('pin.png', -1 )

    #画像urlから画像を取得
    img_map = cv2.imread(url,-1)

    #ブレンド
    dx = 100    # 横方向の移動距離
    dy = 100    # 縦方向の移動距離
    h, w = img_pin.shape[:2]
    img_map[dy:dy+h, dx:dx+w] = img_pin

    return img_map

def geturl():    
    mapdata = getLocation.getLocations()
    _url = mapdata.PoisImage
    return _url

def imread_web(url):
    # 画像をリクエストする
    res = requests.get(url)
    img = None
    # Tempfileを作成して即読み込む
    fp = tempfile.NamedTemporaryFile(dir='./tmp', delete=False)
    fp.write(res.content)
    fp.close()
    img = cv2.imread(fp.name)
    os.remove(fp.name)
    return img

#img = cv2.imread(_url,-1)
_url = geturl()

img = imread_web(_url)
img = cv2.resize(img, dsize=(500, 500))
cv2.imshow("hoge", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


