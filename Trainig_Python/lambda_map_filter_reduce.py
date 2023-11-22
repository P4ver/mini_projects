from functools import reduce
lis = [1, 3, 14, 5, 20, 35]
# lis = [1, 2, 3, 4]

newl = reduce(lambda a,b:a+b, lis)
print(newl)
print(type(newl))


'''
----------------reduce(function, sequence)----------------------
it does not return a list
lis = [1, 2, 3, 4]

newl = reduce(lambda a,b:a+b, lis)
print(newl)
print(type(newl)) #10

----------------filter(function, sequence)----------------------
# filter return true or false

lis = [2, 3, 14, 5, 20, 35]

newlis = list(filter(lambda t: t%5 == 0, lis))
print(newlis) # [5, 20, 35]

newlis = list(filter(lambda t: t >= 5 and t <30, lis))
print(newlis) # [14, 5, 20]

newlis= list(filter(lambda k: k%2 == 0, lis))
print(newlis) # [2, 14, 20]

newlis = list(filter(lambda f: f > 10, lis))
print(newlis) # [14, 20, 35]


----------------map(function, sequence)----------------------
# or do it like this
lis = [2, 14, 20]
nez = list(map(lambda y: y - 2, lis))
print(nez)

# map(function, sequence) #sequence which are list, set, dict  
lis = [2, 14, 20]
squar = map(lambda c: c * 2, lis)
new_lis = list(squar)
print(new_lis)

----------------Lambda----------------------
# it plays the role of anonymous function
add = lambda a, b : a + b
sub = lambda a, b : a - b
mul = lambda a, b : a * b
div = lambda a, b : a / b

print(add(10, 7))
print(sub(6, 4))
print(mul(2, 9))
print(div(20, 4))
'''