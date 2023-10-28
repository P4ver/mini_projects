# 4 - global and local --------------------------------

y = 5

def f():
    print(y)
def g():
    y = 13
    print(y)
def h():
    global y
    y = 96
    print(y)

print(y)#5
f()     #5
print(y)#5
g()     #13
print(y)#5
y = 74
print(y)#74
h()     #96  #the valur of y becomes global
print(y)#96
y = 2       #change the value of y
print(y)#2

# 3 - global and local --------------------------------

y = 5
def aff():
    global y
    y = 13
    print(y)

aff()    # 13

y = 26

print(y) # 26

# 2 - global and local --------------------------------

y = 5

def aff():
    global y
    y = 13
    print(y)

y = 26

aff()    # 13 # because the global is 13
print(y) # 13

# 1 - global and local --------------------------------

y = 5
def aff():
    global y
    y = 13
    print(y)

aff()    # 13
print(y) # 13

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
