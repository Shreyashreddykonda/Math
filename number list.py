def ao():
    z = []
    for i in range(0, 5, 1):
        x = int(input("Enter your number: "))
        z.append(x)
    z.sort()
    max = z[4]
    min = z[0]
    return z, max, min

def do():
    z1 = []
    for i in range(0, 5, 1):
        x1 = int(input("Enter your number to reverse: "))
        z1.append(x1)
    z1.reverse()
    return z1

def fn(first, last):
    c = first + " " + last
    return c
    
m = ao()
print(m)
m1 = do()
print(m1)

fn1 = input("What is your first name? ")
ln1 = input("What is your last name? ")
e = fn(fn1, ln1)
print("Your full name is...")
print(e)





            
