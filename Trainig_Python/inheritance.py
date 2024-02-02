class MyInt(int):
    # def __eq__(self, other):
        # return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)


my_i = MyInt(3)
print(dir(MyInt.__eq__))
print(my_i)
print(my_i == 3)
print(my_i != 3)
    
    
    
    
    
    
#---------------------------------------

# class MyList(list):

    # def append(self, aga):
        # super().append(aga)
    # def print_sorted(self):
        # lis = sorted(self)
        # print(lis)
        

# my_list = MyList()

# print(my_list)      

# my_list.print_sorted()
















# ------------------------------------------

# class MyList(list):
    # def lenn(self):
        # print(len(self))

# my_list = MyList()
#you should use append first
# my_list.lenn()
# print(my_list)

# ------------- inherit from list ------------------

# class MyList(list):
    # def append(self, aga):
        # super().append(aga)
       
# my_list = MyList()
# my_list.append(1)
# my_list.append(4)
# my_list.append(2)        
# print(type(my_list))

#------------make list using inherit---------------------------

# class MyList(list):
    # def append(self, aga):
        # super().append(aga)

# my_list = MyList()
# my_list.append(15)
# my_list.append(50)
# print(my_list) 

#------- EX 2 --------

# class Base():

    # __nb_instances = 0

    # def __init__(self):
        # Base.__nb_instances += 1
        # self.id = Base.__nb_instances

# class User(Base):
    # def __init__(self):
        # self.id = 89
        # super().__init__() #id = 1 because the last call from the father

# u = User()
# print(u.id)

#------- EX ----------
# class Base():
    # __nb_instances = 0

    # def __init__(self):
        # Base.__nb_instances += 1
        # self.id = Base.__nb_instances

# class User(Base):
    # pass

# for i in range(4):
    # u = User()
# print(u.id)

#----------- is subclass -------------

# class A:
    # pass
# class B(A):
    # pass

# print(issubclass(B, A)) #is B is subclass A

#-------------------Iniherit from multi fathers---------------------

# class Place:
    # def __init__(self, city, country):
        # self.city = city
        # self.country = country
    # def exact(self):
        # print("ahl loughlam, bruh!")

# class Person:
    # def __init__(self, first_name, last_name):
        # self.first_name = first_name
        # self.last_name = last_name
        
    # def age(self):
        # print("he is 27 yo")
    
# this class inherits from both Place and Person
# class Info(Place, Person):
    # def __init__(self, city, country, first_name, last_name, ident):
        # Place.__init__(self, city, country)#don't use super() because we have two fathers
        # Person.__init__(self, first_name, last_name)
        # self.ident = ident
    # def more_info(self):
        # Person.age(self)  #call the methode of Person class
        # print("he is 15 yo from child")
        # Place.exact(self) #call the methode of Place class

# obj = Info("casablanca", "morocco", "mohammed", "habti", 1200)

# obj.more_info()

# print(isinstance(obj, object))
# print(type(obj) is object)

# ------------------ inherit from moro than one father-----------------------

# class Place:
    # def __init__(self, city, country):
        # self.city = city
        # self.country = country
# class Person:
    # def __init__(self, first_name, last_name):
        # self.first_name = first_name
        # self.last_name = last_name
    
## this class inherits from both Place and Person
# class Info(Place, Person):
    # def __init__(self, city, country, first_name, last_name, ident):
        # Place.__init__(self, city, country)        #don't use super() because there are two fathers
        # Person.__init__(self, first_name, last_name)
        # self.ident = ident

# obj = Info("casablanca", "morocco", "mohammed", "habti", 1200)

# print(obj.city)

# ------------------ overriding variable -----------------------

# class Animal:
    # color = "white"

# class dog(Animal):
    # color = "orange"


# animal_one = dog()
# print(animal_one.color)

# ------------------ overriding methode ----------------------

# class Animal: # superclass
    # def sound(self):
        # print("this is how could dog sound")

# class dog(Animal): # subclass
    # def sound(self):
        # print("woof woof!")

# creat instance of the subclass
# animal_one = dog() 

# animal_one.sound() #this will overide the method in the father

#----------------------------------

# class Car:
    # def __init__(self, make, model, year):
        # self.make = make
        # self.model = model
        # self.year = year
        
    # def start(self):
       # print(f"{self.make} // {self.model} start in {self.year}")
    
# class Elec(Car): 
    # def __init__(self, make, model, year, speed, battery):
        # super().__init__(make, model, year) # call the constructor of the father
        # self.speed = speed
        # self.battery = battery
    # def country(self): #the mothede in the child we can not call it from the father obj
        # print(f"{self.make} from USA")

# inf = Car("dacia", "logan", 2012)
# car1 = Elec("tesla", "x1",2018, "260km/h","2000wma") #creat instance of the subclass

# inf.start() 
# car1.start() #the child can call everything from the father
# car1.country() 

# print()

# print(car1.make)
# print(car1.model)
# print(car1.year)
# print(car1.speed)
# print(car1.battery)

# print(dir(inf)) #display attribute and methodes in the class father
# print(dir(car1)) #display attribute and methode in the class child


# ---------------------------------
# IMPORTANT
# ---------------------------------


# class Org:
    # def __init__(self):
        # print("mohammed habti")
    # def age(self):
        # print("27")

# class Chi(Org):
    # def __init__(self):
        # super().__init__()
        # super().age()     #first way to call method
        # Org.age(self)       #second way to call method
        # print("from morocco")
    # def info(self):
        # print("========")
        # super().age()
        # Org.__init__(self)
        # print("========")
    
# prnt = Chi()
# prnt.info()


# ---------------------------------
# ---------------------------------

# class Car:  # ==> define superclass
    # def __init__(self, make, model, year):
        # self.make = make
        # self.model = model
        # self.year = year

# ==> define subclass
# class Elec(Car): # class Elec is a child of class Car
    # pass

# either this or obj = Car(...) will work 
# obj = Elec("tesla", "x1","2018") #creat instance of the subclasss

# print(obj.make)

