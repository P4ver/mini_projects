st = {2, 5, 6, 7, 8, 9, 'mohammed', 'habti'}
set2 = {1996,1949,"habti", 5 ,2, 9}
set3 = {5,22,"habti", "mohammed" , 9,2}

new_st = st & set2
print(new_st)

'''
# ---------------------------------------------------
# that will show the element that are not in commun
# this is opposite of "intersection" or '&'

st = {2, 5, 6, 7, 8, 9, 'mohammed', 'habti'}
set2 = {1996,1949,"habti", 5 ,2, 9}

new_st = st ^ set2 # or use se.symmetric_difference(set2)
print(new_st) # {7, 6, 8, 1996, 'mohammed', 1949}


# ---------------------------------------------------
if you wanna make difference between than two
st = {2, 5, 6, 7, 8, 9, 'mohammed', 'habti'}
set2 = {1996,1949,"habti", 5 ,2, 9}
set3 = {5,22,"habti", "mohammed" , 9,2}

new_st = st - set2 - set3
print(new_st) # {8, 6, 7}


# the difference will remove all the commun element 
  between two set in the first set
  
st = {2, 5, 6, 7, 8, 9, 'mohammed', 'habti'}
set2 = {1996,1949,"habti", 5 ,2, 9}

new_st = st - set2 #or use new_st = st.difference(set2)
print(new_st)

# ---------------------------------------------------

# the second way to return only commun element of a lot of set 

st = {'mohammed', 2, 5, 6, 7, 8, 9, 'habti'}
set2 = {1996,1949,"habti", 5 ,2}
set3 = {5,22,"habti", "mohammed" ,2}
new_set = st & set2 & set3 
print(new_set) # {2, 'habti', 5}


# intersection return new set with commun element

st = {'mohammed', 2, 5, 6, 7, 8, 9, 'habti'}
set2 = {1996,1949,"habti", 5 ,2}

print(new_set) # {2, 'habti', 5}

# ---------------------------------------------------

# second way to merge a lot of set
set1 = {"a", "n" , "habti"}
set2 = {10,5,6}
set3 = {5.5, 0.3, 7.9}
new_set = set1 | set2 | set3
print(new_set)

# union merge two set

set1 = {"a", "n" , "habti"}
set2 = {10,5,6}
new_set = set1.union(set2)
print(new_set) #{'a', 'n', 5, 6, 10, 'habti'}

# ---------------------------------------------------

# new_set = set.copy()
# will all element of the set to the new_set
new_set = st.copy()
print(new_set) #{2, 'habti', 5, 6, 7, 8, 9, 'mohammed'}
# ---------------------------------------------------

# set.clear() will clear all element, making it empty
st.clear()
# ---------------------------------------------------

# remove and return the element was removed
st.pop()
print(st)
# ---------------------------------------------------

# set.discard(element) #remove if it is found if not found
# will not raise the error unlikely remove()
st.discard(8)
print(st)
# ---------------------------------------------------

# set.remove(element) 
st.remove("habti")#the value of the element to be removed
print(st)
# ---------------------------------------------------

# set.add(element)   ,to add element to the set

st.add(1996)
st.add("casablanca")
print(st)
st.add(True)
# ---------------------------------------------------

st = {8,"habti", 2 ,5 ,2 ,6,9,5,7,"mohammed",6,2,"habti"}
#it will show the result in different order
print(st)#{2, 'mohammed', 5, 6, 7, 8, 9, 'habti'}
'''
