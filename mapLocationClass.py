import LocationClass

class MapLocation:   
    def __init__(self,id,name,x = 0,y = 0,z = 0):
        self.__id = id
        self.__name = name
        self.__location = LocationClass.Location(x,y,z)

    @property
    def id(self):
        return  self.__id
    
    @property
    def name(self):
        return  self.__name
    
    @property
    def location(self):
        return self.__location  
    

    