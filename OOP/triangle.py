import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x 
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.sqrt((self.__x - x)**2 + (self.__y - y)**2)

    def distance_from_point(self, point):
        x_point = point.getx()
        y_point = point.gety()
        # return Point.distance_from_xy(self, x_point, y_point)
        return self.distance_from_xy(x_point, y_point)



class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertice1 = vertice1
        self.__vertice2 = vertice2
        self.__vertice3 = vertice3
    def perimeter(self):
        len12 = self.__vertice1.distance_from_point(self.__vertice2)
        len13 = self.__vertice1.distance_from_point(self.__vertice3)
        len23 = self.__vertice2.distance_from_point(self.__vertice3)

        perimeter = len12 + len13 + len23
        return perimeter

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
