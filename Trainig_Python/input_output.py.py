






# print(m.__dict__) #show attribute of a class as dictionary


# print(len(m.__dict__)) #the number of attribute
#----------------------------------------------------
#----------------------------------------------------

# import json

# class Mycls:
    # def __init__(self, name, age):
        # self.name = name
        # self.age = age

# obj = Mycls("mohammed", 32)

# with open("simsim.json", "w") as nfl:
    # nfl.write(json.dumps(obj.__dict__))
    
         # --------LOAD ----------
    
# with open("simsim.json", "r") as nfl:
    # print(json.load(nfl))


# --------------- all resume -----------

# import json

# data = {"name":"mohammed", "age": 27, "degree":"bac+3"}

# convert python dict to json
# cnv_to_jsn = json.dumps(data)

# add string json to file .json
# with open("data.json", "a") as fl:
    # fl.write(cnv_to_jsn)
    
# print(cnv_to_jsn)    
# print(type(cnv_to_jsn))    

# read  
# with open("data.json" , "r") as rd_file:
    # load = json.load(rd_file)
# print(load)
# print(type(load))   

# ----------------------------------------------

# import json
    
# with open("data.json" , "r") as rd_file:
    # load = json.load(rd_file)
# print(load) 
# print(type(load)) # <class 'dict'>     

# -------------- convert dict python to json ---------------

# import json

# data = {"name":"mohammed", "age": 27, "degree":"bac+3"}

# convert python dictionary to json
# print(json.dumps(data)) # displays string

# -----------------------------------------------------     

# -----------------------------------------------------
     
# -----------------------------------------------------     
# with open("gava.txt", "r") as file:
    # data = file.read()
    
# print(data, "\n==========") # just display at the end not add
    
# move the cursor in file ----------------------------------- 
    
# with open("gava.txt", "r") as file:
    # file.seek(10)
    # data = file.read()
    
# print(data)    
    
# ---------------- READ FILE ----------------------

# with open("gava.txt", "r") as new_file:
    # ln = new_file.readline()
    # while ln:
        # print(ln.strip())
        # ln = new_file.readline()

# -------------- READ FILE (the easiest way)----------------------------------------------
    
# with open("gava.txt", "r") as new_file:
    # print(new_file.read())
    
# -------------- READ FILE (easy way----------------------------

# with open("gava.txt", "r") as new_file:
    # for line in new_file:
        # print(line.strip())
 
# -------------- WRITE and ADD CONTENT-----------------------------------------------
# with open("gava.txt", "a") as new_file:
    # new_file.write("the fourth edit\n")

# -------------- WRITE and ADD CONTENT-----------------------------------------------
    
# new_file = open("gava.txt", "a")
# new_file.write("the third edit ,let's try again \n") # add content at the end the previeus content     
  
# -------------- WRITE CONTENT-----------------------------------------------
    
# new_file = open("simo_new.txt", 'w')        
# new_file.write("mohammed hatbi next level")  # write the content override the previeus content 

#-----------------------------------------------

# with open('ha.txt', 'w') as file:
    # file.write("hello from input file")   