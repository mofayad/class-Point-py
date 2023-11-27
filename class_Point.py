import math 
class Point :
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x

    def setX(self, new_x):
        self.x = x

    def getY(self):
        return self.y

    def setX(self, new_y):
        self.y = y

    def Distance(self, point):
        dx = self.x - point.getX()
        dy = self.y - point.getY()
        return math.sqrt(dx**2 + dy**2)

    def Norme(self):
        return math.sqrt((self.x)**2 + (self.y)**2)


p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1.Distance(p2))
print(p1.Norme())