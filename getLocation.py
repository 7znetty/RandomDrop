import json
import requests
import pprint
import MapDataClass
import mapLocationClass

def getLocations():
    request = getRequests()
    if request.status_code == 200:
        content = json.loads(request.text)
        #return content["data"]["images"]["blank"]
        mapData = MapDataClass.MapData(content["data"]["images"]["blank"],content["data"]["images"]["pois"])
        for data in content["data"]["pois"]:
            id = data["id"]
            name = data["name"]
            x = data["location"]["x"]
            y = data["location"]["y"]
            z = data["location"]["z"]
            location = mapLocationClass.MapLocation(id,name,x,y,z)
            mapData.appendData(location)

        return mapData
    else:
        return "error"
    
#getLocations用
def getRequests():
    url = "https://fortnite-api.com/v1/map?language=ja"
    req = requests.get(url)
    return req

#getLocations用
def ConvertLocation(id,name,x,y,z):
    data = MapDataClass.MapData(id,name,x,y,z)
    return data

def FindNamedLocation(mapDataList,isAllLocation = False):
    #isAllLocation = Trueなら全部の街を返す
    if isAllLocation:
        return mapDataList
    else:
        list = []
        text = "Athena.Location.POI"
        for data in mapDataList:
            id = data.id
            if text in id:            
                list.append(data)
        return list