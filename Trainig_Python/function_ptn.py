

# ------------------------------------------------
def sign(a, b):
    if a*b>0:
        print("the product is positive ")
    else:
        print("the product is negative ")
def min(a, b):
    if a > b:
        mini = b
    else:
        mini = a
    return mini
def max(a, b):
    if a > b:
        maxi = a
    else:
        maxi = b
    return maxi

a = int (input("enter the number "))
b = int (input("enter the number "))

sign(a, b)
print("the min is ", min(a, b))
print("the max is ", max(a, b))

# ------------------------------------------------

def text(str):
    u = "Hey Mr. "
    return u + str

str = input("Enter your full name : ")
ch = text(str)    
print(ch)

# ------------------------------------------------
def name(nm):
    print("Hey", nm)

name("mohammed")
# ------------------------------------------------

def simo():
    print("hey mohammed habti")

def calc(u, i):
    return u + i

simo()

p = calc(5, 6)
print(p)
