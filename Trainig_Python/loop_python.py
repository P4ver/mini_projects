# the table of mult using users num -------------

u = int(input("enter a num = "))

while u <= 0 or u > 10:
    u = int(input("enter another num = "))

for m in range(1, 11):
    print(u,"*",m,"=", u * m)

#the good example to understand end ------------

for i in range(1,5):
    for j in range(1, 5):
        print("*", end=" . ") # " . " after each "*" 
    print("$")                # "$" at the end of each line

#  the output will be :

#  * . * . * . * . $
#  * . * . * . * . $
#  * . * . * . * . $
#  * . * . * . * . $

# print patern using stars----------------------
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print("")

# print square ---------------------------------
for i in range(4):
    for j in range(4):
        print("*", end="") # put what you want inside end to be after '*'
    print("") # the end of every line and go to the next line

# the sum with user number ----------------------
k = int (input("enter the number that you wanna calc its sum from zero "))
s = 0
for i in range(k+1):
    s = s + i
print(s)

# calc the sum of 20 first numbers ---------------
s = 0
for i in range(21):
    s = s + i
    print(s)

# calc the mult of a num -------------------------
n = int (input("enter the number n "))

for i in range(10):
    print(n,"*",i,"=",n * i)

# the tabel of mult------------------------------
for i in range(1,10):
    for j in range(1,10):
        print(i, "*", j, "=", i * j)
    print("-------------")

# mult of 7--------------------------------------
for i in range(10):
    print("7 *",i,"=", 7 * i)

# --------------------

for i in range(4):
    print("Hello world")
for i in range(0, 4):
    print("Mohammed")
for i in range(0, 4, 1):
    print("Habti")

# 5 to 1 ----------------------------------------
for i in range(5, 0,-1):
    print(i)

# from 6 to 40 with 3 increas -------------------
for i in range(6, 40, 3)
    print(i)

# from 5 to 12 ----------------------------------
for i in range(5, 13)
    print(i)
# i = 0 to 4 ------------------------------------
for i in range(5):
    print(i)

# -----------------------------------------------
country = "morocco"
for i in country:
    print(i)
# -----------------------------------------------
