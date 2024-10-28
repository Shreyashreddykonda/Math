class rat():
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def hypotanuse(self):
        self.h1 = ((self.b * self.b) + (self.h * self.h)) ** 0.5
        return self.h1
    def perimeter(self):
        self.p = self.h + self.b + self.h1
        return self.p
    def area(self):
        self.a = (self.b * self.h) / 2
        return self.a

t1 = rat(3, 4)
z1 = t1.hypotanuse()
z2 = t1.perimeter()
z3 = t1.area()

t2 = rat(100, 322)
z4 = t2.hypotanuse()
z5 = t2.perimeter()
z6 = t2.area()

z7 = z2 + z5
z8 = z3 + z6
z9 = z1 / z4

print("The hypotanuse of the triangle is...")
print(z1)
print("The perimeter of the triangle is...")
print(z2)
print("The area of the triangle is...")
print(z3)

print("The hypotanuse of the second triangle is...")
print(z4)
print("The perimeter of the second triangle is...")
print(z5)
print("The area of the second triangle is...")
print(z6)

print("The combined sum of the two perimeters is...")
print(z7)
print("The combined sum of the two areas is...")
print(z8)
print("The ratio of the two hypotanuses is...")
print(z9)

print(t1.r)
        
    
