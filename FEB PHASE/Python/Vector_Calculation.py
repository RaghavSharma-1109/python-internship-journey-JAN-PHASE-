class Vector():
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def __add__(self,other):
        return Vector(self.x + other.x, self.y+other.y)
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)
    def __mul__(self,scaler):
        return Vector(self.x*scaler, self.y*scaler)
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

v1 = Vector(2,3)
v2 = Vector(4,5)

print(v1 + v2)
print(v1 - v2)
print(v1 * 3)