a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }

z = a["friends"][-1]["name"]
g = a.get("friends")[-1].get("name")
print(z) # Amy
print(g) # Amy
'''
----------------- GET ----------------------
a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }

z=a["friends"][-1]["name"]
print(z) # 


get the value of the name if it found if not give "none"
d.get("country", "none") # none
-----------------------------------------
# another way to display values and keys
for a,b in dict.items():
    print("key :", a)
    print("value :", b)
    
key : name
value : mohammed
key : age
value : 27
key : university
value : ben m'sik

--------iterating over items -----------------
# loop to display both values and keys
for ele in dict.items():
    print(ele)
    
# ('name', 'mohammed')
# ('age', 27)
# ('university', "ben m'sik")
    

--------iterating over values -----------------
# loop to display only values 
for value in dict.values():
    print(value)

# mohammed
# 27
# ben m'sik

#--------iterating over keys -------------------
# loop to display only key element not thier values
for key in dict:
    print(key)

# name
# age
# university

#-----------------------------------------

# to delet an element
del dict["university"]
print(dict)
#or you can use pop method
dict.pop("university")
print(dict)

#-----------------------------------------
# add a new element to the dictionary
dict["city"] = "casablanca"
print(dict)

#-----------------------------------------
change the value
dict["name"] = "abdelkader"
print(dict["name"])

#-----------------------------------------

dict = {"name":"mohammed", "age": 27, "university": "ben m'sik"}
print(dict) # or 
print(dict["name"])
print(dict["age"])
print(dict["university"])
#-------------------------------------------
a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
a.get('projects')[3] # 4
a["projects"][3] # 4
#-------------------------------------------
a.get("name", 0) # if the ele found put its value if not put 0

'''