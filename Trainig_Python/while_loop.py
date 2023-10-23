# (Continue) example to calc sum -------------------------

s = 0
for i in range(1, 8):
    print("enter a num ", i,"= ", end="")
    j = int(input())
    if j <= 0:
        continue
    s = s + j
print(s)

# (Break) example to calc sum ----------------------------

i = 0
s = 0
while i < 8:
    print("enter the num ",i,":", end="")
    h = int (input())
    if h >= 0:
        s = s + h
    else:
        break
    i = i + 1
print(s)

# enter the positive num and calc sum ---------------------

h = int(input("enter any num "))
i = 0
s = h
while i < 8:
    h = int (input("enter any positive num "))
    if h >= 0:
        s = s + h
    else:
        break
    i = i + 1
print(s)

# calc the sum from 0 to user num ------------

h = int (input("enter the num "))
s = 0
i = 0

while h < 0:
    h = int(input("enter a positive num "))

if h > 0:
    while i < h + 1:
        s = s + i
        print(i,end="")
        if i != h:
            print(end="+")
        elif i == h:
            print(end="=")
            print(s, end="")
        i += 1

# the output:
# 0+1+2+3+4+5+6+7+8+9+10=55

# enter the num between 10 and 20 ------------

h = int (input("enter the num "))

while h<10 or h > 20:
    if h < 10:
        print("smaller")
    elif h > 20:
        print("bigger")
    h = int(input("enter another one "))
print("BRAVO , you typed a num between 10 and 20 ", end="!")

# --------------------------------------------

u = int(input("enter a num = "))

while u <= 0 or u > 10:
    u = int(input("enter another num = "))
m = 1
while m <= 10:
    print(u,"*",m,"=", u * m)
    m += 1

# --------------------------------------------

u = int(input("enter a num = "))

while u <= 0 or u > 10:
    u = int(input("enter another num = "))

for m in range(1, 11):
    print(u,"*",m,"=", u * m)
