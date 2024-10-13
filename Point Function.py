class Point:

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"
    
#Create Object
p1 = Point(2,3)
p2 = Point(33, 69)
p3 = Point(75, 25)

print(p1)
print(p2)
print(p3)