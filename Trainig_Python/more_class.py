class Rectangle:
    number_of_instances = 0
    print_symbol = '#'
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        
        Rectangle.number_of_instances += 1
        
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height
        
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        return self.__height * self.__width
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
    
    def __str__(self):
        val = self.print_symbol
        if self.__height == 0 or self.__width == 0:
            return ""
        elif type(self.print_symbol) is list:
            return "\n".join(
                [str(val) * self.__width for i in range(self.__height)]
            )
        elif type(self.print_symbol) is int:
            k = str(self.print_symbol)
            return '\n'.join(k * self.__width for i in range(self.__height))
        else:
            return "\n".join([self.print_symbol * self.__width for i in range(self.__height)])
    
    def __repr__(self):
        return "Rectangle({},{})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        a_1 = rect_1.__width * rect_1.__height
        a_2 = rect_2.__width * rect_2.__height
        if a_1 >= a_2:
            return rect_1
        else:
            return rect_2
    @classmethod
    def square(cls, size=0):
        return cls(size, size)



my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)










#--------- call from the class -------------------
# class Chi:
    # def __init__(self):
        # print("from morocco")
        # self.info()
    # def info(self):
        # print("========")
        # print("hey from info")
        # print("========")
    
# prnt = Chi()

#IMPORTANT-----------------------------------------
# obj = MyClass(1, 2, 3)
# print(obj.__dict__) #show attribute of a class 
# print(len(obj.__dict__)) #the number of attribute

#or

# print(vars(obj))
# print(len(vars(obj)))



# ---------------the number of instance-------------
# class Rectangle:
    # number_of_instances = 0
    # def __init__(self, width=0, height=0):
        # self.height = height
        # self.width = width
        # Rectangle.number_of_instances += 1

# --------------Delete an Object -------------------
    # def __del__(self):
        # print("Bye Object ...")
#  __doc__ Accessing the docstring----------------------

# def my_function():
    # """This is the documentation string for my_function."""
    # print("Hello, World!")

# print(my_function.__doc__)

# __repr__(): devloper friendly repsentaion -------------

# class Inf:
    # def __init__(self, firstname):
        # self.firstname = firstname

    # def __repr__(self):
        # return f"Inf('{self.firstname}')"

# obj = Inf("pales")
# print(repr(obj))

# __str__(): user friendly repsentaion -----------------
# class Hyt:
    # def __init__(self, name):
        # self.name = name
    # def __str__(self):
        # return f"my name is {self.name}"

# obj = Hyt("mohammed")

# print(str(obj))
# print(obj.__str__())

# @staticmethod -------------------------
# class Student:
    # @staticmethod
    # def add(a, b):
        # return a + b
    # @staticmethod
    # def sub(a, b):
        # return a - b

# sum = Student.add(60, 5)
# sous = Student.sub(20, 9)

# print(sum)
# print(sous)

# setter - getter - deleter ---------------------
# class Mo:
    # def __init__(self, name):
        # self.__name = name
    
    # @property
    # def name(self):
        # return self.__name
    # @name.setter
    # def name(self, val):
        # self.__name = val
    # @name.deleter
    # def name(self):
        # print("it is deleted")
        # self.__name = None
        
# obj = Mo("abdelkader")
# print(obj.name)

# obj.name = "mohammed"
# print(obj.name)

# del obj.name
# print(obj.name)
