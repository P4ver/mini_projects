class person:
    #class attribute
    city = "morocco"
    
    def __init__(self, name,age):
        self.age = age #binding attribute to object
        self.name = name

inf = person("mohammed", 30)

print(getattr(person, "city"))




















'''
----------------------------------------------------------

#getattr(class or obj, "attribute", "value if u have new attr")
class person:
    #class attribute
    city = "morocco"
    
    def __init__(self, name,age):
        self.age = age #binding attribute to object
        self.name = name

inf = person("mohammed", 30)

print(getattr(inf, "name")) # dispaly the value of name 
print(getattr(person, "simo", "uuiii")) #add a new attribute with its value
print(getattr(person, "year", 2023))
print(getattr(inf, "yo", 2050))
print(getattr(person, "city"))

-------------------------------------------------------
class person:
    #class attribute
    city = "morocco"
    
    def __init__(self, name,age):
        self.age = age #binding attribute to object
        self.name = name

inf = person("mohammed", 30)

print(getattr(inf, "name"))
print(getattr(person, "simo", "uuiii"))

----------------------------------------------------

#dictionary to show instance
class person:
    #class attribute
    city = "morocco"
    
    def __init__(self, name,age):
        self.age = age #binding attribute to object
        self.name = name

inf = person("mohammed", 30)
print(inf.__dict__) # {'age': 30, 'name': 'mohammed'}

------------------------------------------

#dictionary to show class
class person:
    #class attribute
    city = "morocco"
    
    def __init__(self, name,age):
        self.age = age #binding attribute to object
        self.name = name
        
print(person.__dict__) #dictionary that contains attribute or instance of class
___________________________________________
#class attribute 

class person:
    #class attribute
    _city = "casablanca"
    
    def __init__(self, name,age):
        self.age = age #binding attribute to object
        self.name = name

#creat an instance
pr1 = person("mohammed", 45)
pr2 = person("alice", 23)

#acces attribute of object
print(pr1.name) #mohammed
print(pr2.age) #23
 
#access class attribute
print(pr1._city) # casablanca
print(pr2._city) # casablanca
# print(pr3.city) #will raise an error 'cause we have only two objects

---------------------------------------------------------
class person:
    #class attribute
    _city = "casablanca"
    
    def __init__(self, name,age):
        self.age = age #binding attribute to object
        self.name = name

#creat an instance
pr1 = person("mohammed", 45)
pr2 = person("alice", 23)

#access class attribute
print(pr1._city) # casablanca
print(pr2._city) # casablanca
# print(pr3.city) #will raise an error 'cause we have only two objects


----------------------------------------------
#adding attribute

class person:
    def __init__(self, age):
        self.age = age

#creat an instance
obj = person(45)

print(obj.age)           


# adding new attribute
obj.counter = 444
print(obj.counter)

obj.name = "mohammed"
print(obj.name)

obj.lastname = "habti"
print(obj.lastname)


-----------------------------------------------
# using deleter 
class person:
    def __init__(self, age):
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, newAge):
        if newAge < 18:
            raise ValueError("you should not be here")
        self._age = newAge
    @age.deleter
    def age(self):
        print("the age value is deleted")
        del self._age

obj = person(27)
print(obj.age) # using the property

obj.age = 20
print(obj.age) # using property setter if not true

del obj.age # the property using deleter  
print(obj.age) #object has no attribute '_age'

----------------------------------------------------
# getting and setter

class person:
    def __init__(self, age):
        self._age = age
    
    @property                # getting 
    def age(self):
        return self._age
    
    @age.setter
    def age(self, newAge):
        if newAge < 18:
            raise ValueError("you should not be here")
        self._age = newAge

obj = person(27)
print(obj.age) # using the property

obj.age = 20
print(obj.age) # using property setter if not true

obj.age = 12
print(obj.age) # using property setter and will raise an error

-----------------------------------------------------
# getting and setter

class car:
    def __init__(self, Name):
        self._Name = Name # attribute protected
    @property #using at getting
    def Name(self):
        return self._Name
    @Name.setter
    def Name(self, new_Name):
        if new_Name < 10:
            raise ValueError("you made a mestake")
        self._Name = new_Name

obj = car(14)
print(obj.Name) #using the property 

obj.Name = 18 
print(obj.Name)#using the property setter with validation

------------------------------------------------------
# getting and setter

class car:
    def __init__(self, Name):
        self._Name = Name # attribute protected
    @property #using at getting
    def Name(self):
        return self._Name
    @Name.setter
    def Name(self, new_Name):
        if new_Name != "fiat":
            raise TypeError("you made a mestake")
        

obj = car("mercedis")

#using the property setter width validation
obj.Name = "renault" #this will raise an error 
print(obj.Name)
------------------------------------------

class calcArea:
    def __init__(self, height, width): #the height and width are attribute
        self.height = height
        self.width = width

    def rectangle(self):
        return self.height * self.width
    def circle(self):
        return self.height * (3.14 ** 2)

#creat an instance
mis = calcArea(5, 9)
cir = calcArea(10,0)

#calling the method to calc
print(mis.rectangle())
print(cir.circle())


-----------------------------------------------------

class person:
    def __init__(self, firstname):
        self.__firstname = firstname  # privet attribute 
    def get_name(self):
        return self.__firstname

obj = person("mohammed")

print(obj.get_name())






------------------------------------------------------

class person:
    def __init__(self, firstname, lastname):
        self._firstname = firstname # protected attribute
        self._lastname = lastname
    def show_name(self):
        return self._firstname
    def last_name(self):
        return self._lastname

obj = person("khabib", "nurmagomedov")

get_last_name = obj.last_name()

get_firs_name = obj.show_name()

print(get_firs_name)
print(get_last_name)
-------------------------------------------

class student:
    def __init__(self, name, age):
        self.name = name  # public attribute 
        self.age = age

#creat an instance
#obj = class()        
st1 = student("mohammed", 27)


print(st1.name)
print(st1.age)
'''