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
