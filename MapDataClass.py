import mapLocationClass

class MapData:
    __data = []

    def __init__(self,blank,pois):
        self.__blank = blank
        self.__pois = pois

    @property
    def BlankImage(self):
        return self.__blank
    
    @property
    def PoisImage(self):
        return self.__pois
    
    @property
    def data(self):
        return self.__data
    
    def appendData(self,data):
        self.__data.append(data)

