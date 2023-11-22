
#-------------------------------------------

#remove and return the spcified number 
numlist = [12,3,64,984,6,5,49]
numlist.pop()#remove and return the last item # 49
numlist.pop(2)#remove the item 2 which is 64 and return 64 

#-------------------------------------------

#change the lelement value or delet or change the size of element
'''        0  1  2  3  4 5 6  '''
numlist = [12,3,64,984,6,5,49]
numlist[2:5] = ['c','d','e'] #change the element[12, 3, 'c', 'd', 'e', 5, 49]
numlist[2:5] = ['A', 'B'] #change the size [12, 3, 'A', 'B', 5, 49]
numlist[2:5] = [] #delet [12, 3, 49]
numlist[:] = [] #clear the list

#-------------------------------------------
# append  equivalent to a[len(a):] = [x].
lett=['a','b','c','d','e']
lett.append('f') #will add new element
#a[len(a):] = ['f'].  
lett.append(187)
#a[len(a):] = [187].


#-------------------------------------------
# displaying list[start: stop: step]

lis = [12,3,64,984,6,5,49]

print(lis)

print(lis[:5])  # display list from 0 to 5
print(lis[::3]) # display list from 0 to end with 3 step
print(lis[:7:2])# display list from 0 to 7 with 2 steps
print(lis[-1:-4:-1])# display list from -1 to -4 (it is madatory to select step)  

# displaying list
#        -4         -3    -2  -1
li = ['mohammed', 'habti', 3, 122]

print(li)
print(li[0])
li[-4] = 'morocco'
print(li)
# display the last element
print(li[-1])

# the fourth way to creat a list
#--------list(range(start, stop, step))
list_3 = list(range(3, 20, 1))
print(list_3)

# the third way to creat a list
newlis = list("hello,")
print(newlis)# ['h', 'e', 'l', 'l', 'o', ',']

"""
the difference between first and second
the second when i put one element

#           01234            
li = list(('habti'))

"""
# the second way to creat a list

list_2 = list(('moha', 'habti', 4, 8.7))
print(list_2)

# the first way to creat a list
list_1 = ['qnq','mohammed', 'habti', 'casablanca']
print(list_1)
