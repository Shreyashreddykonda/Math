def rat(b, h):
    hyp = ((b ** 2) + (h ** 2)) ** 0.5
    area = b * h * 0.5
    perimeter = hyp + b + h
    return hyp, area, perimeter

def num(a, b, c, d, e, f, g, h, i, j):
    sum = a + b + c + d + e + f + g + h + i + j
    average = (a + b + c + d + e + f + g + h + i + j) / 10
    return sum, average

def sqr(n):
    z = n ** 0.5
    return z

a = float(input("Enter the base of the triangle (in cm) "))
x = float(input("Enter the height of the triangle (in cm) "))
z = rat(a, x)
z1a = z[1]
z1h = z[0]
z1p = z[2]

print("The the hypotenuse, area and perimeter of the triangle is:")
print(z)
print("The area in sq cm is:")
print(z1a)
print("The perimeter in sq cm is:")
print(z1p)
print("The hypotenuse in sq cm is:")
print(z1h)

z2 = rat(17, 19)
z2a = z2[1]
z2h = z2[0]
z2p = z2[2]
z12 = z1a + z2a
print("The the hypotenuse, area and perimeter of the triangle is:")
print(z2)
print("The area in sq cm is:")
print(z2a)
print("The perimeter in sq cm is:")
print(z2p)
print("The hypotenuse in sq cm is:")
print(z2h)
print("The sum of the two cricles is:")
print(z12)

s1 = float(input("Enter the first number "))
s2 = float(input("Enter the second number "))
s3 = float(input("Enter the third number "))
s4 = float(input("Enter the fourth number "))
s5 = float(input("Enter the fifth number "))
s6 = float(input("Enter the sixth number "))
s7 = float(input("Enter the seventh number "))
s8 = float(input("Enter the eighth number "))
s9 = float(input("Enter the ninth number "))
s10 = float(input("Enter the tenth number "))
ss = num(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10)
ss10 = s10 * s10
print("The sum and average of the two numbers are...")
print(ss)
print("The square of the last number is...")
print(ss10)

aa = sqr(11)
print(aa)





