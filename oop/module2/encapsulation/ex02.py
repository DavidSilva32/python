# Control amounot of circle
class Circle:
    __circles_total = 0

    def __init__(self, pointx, pointy, radius):
        self.pointx = pointx
        self.pointy = pointy
        self.radius = radius
        self.__circles_total += 1

    @classmethod
    def get_circles_total(cls):
        return cls.__circles_total    
