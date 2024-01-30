class Location:
    def __init__(self,x,y,z):
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def z(self):
        return self.__z