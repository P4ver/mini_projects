# import unittest
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("mmust be string")
    punctuation = {'.', '?', ':'}
    current_line = ""

    for char in text:
        current_line += char
        if char in punctuation:
            print(current_line.strip())
            print() 
            current_line = ""

    if current_line:
        print(current_line.strip())
       
text_indentation(15616)



# if __name__ == "__main__":
    # import doctest
    # doctest.testfile(ex_doctest.txt)
    
    
    
###############################################    
    
# _____________________________________________
# ---- Unittest -------------------------------
# ------------------ Only Python File ---------

# import unittest
# add = __import__('p1').add
# class Testadd(unittest.TestCase):
    # def test_bs(self):
        # self.assertEqual(add(20,1), 20)

# if __name__ == '__main__':
    # unittest.main()

# ------------------ Compile ------------------
# python p2.py

# #############################################

# _____________________________________________
# ---- Doctest --------------------------------
# ------------------ Python File --------------

# def add(x, y):
    # return x + y
    
# if __name__ == '__main__':
    # import doctest
    # doctest.testfile("tst.txt")

# ------------------ text file ----------------

	# >>> add = __import__('p1').add

	# >>> add(10, 6)
	# 15
    
# ------------------ Compile ------------------
# python p1.py    
    
    
    
    
#4 --------------------------------------------
# def print_square(size):
    # if not type(size) is int:
        # raise TypeError("size must be an integer")
    # if size < 0:
        # raise ValueError("size must be >= 0")
    # if type(size) is float:
        # raise TypeError("size must be an integerQQQQ")
    # if size == 0:
        # print()
    # else:
        # for i in range(size):
            # print("#" * size)

# print_square(4)
# print("")
# print_square(10)
# print("")
# print_square(0)
# print("")
# print_square("a")
# print("")
# print_square(-1)

# try:
    # print_square(-1)
# except Exception as e:
    # print(e)
# print("")
# try:
    # print_square(-1.5)
# except Exception as e:
    # print(e)
# print("")

# 3 -------------------------------------------
# def say_my_name(first_name, last_name=""):
    # if not (type(first_name) is str):
        # raise TypeError("first_name must be a string")
    # if not (type(last_name) is str):
        # raise TypeError("last_name must be a string")
    
    # print("My name is {} {}".format(first_name, last_name))

# say_my_name("John", "Smith")
# say_my_name("Walter", "White")
# say_my_name("Bob")
# try:
    # say_my_name(12, "White")
# except Exception as e:
    # print(e)


#2----------------------------------------------

# def matrix_divided(matrix, div):
    # if type(div) not in (int, float):
    # if not isinstance(div ,(int, float)):
        # raise TypeError("div must be a number")
    # if div == 0:
        # raise ZeroDivisionError("division by zero")
    
    # if not(isinstance(matrix, list) and all(type(h) is list for h in matrix) and all(type(j) in (int, float) for i in matrix for j in i)):
        # raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # if not all(len(rw) == len(matrix[0]) for rw in matrix):
        # raise TypeError("Each row of the matrix must have the same size")
    # lt = list(map(lambda rw: list(map(lambda q: round(q/div,2), rw)), matrix))
    # return lt

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]

# print(matrix_divided(matrix, 2))
# print(matrix)


# 0 ---------------------------------------
# def add_integer(a, b=98):
    # if not(isinstance(a, int) or isinstance(a, float)):
    # if type(a) not in (int, float): 
        # raise TypeError("a must be an integer")
    # if type(b) not in (int, float):
        # raise TypeError("b must be an integer")
    # c  = int(a) + int(b)
    # return c

# print(add_integer(1, 2))
# print(add_integer(100, -2))
# print(add_integer(None))
# print(add_integer(float('inf'), 15))

# try:
    # print(add_integer(float('inf'), "habtii"))
# except Exception as e:
    # print(e)
# try:
    # print(add_integer(None))
# except Exception as e:
    # print(e)

#----------------------------------------------
# IMPORTANT: to check we put 
# python filename.py
# if it is false will show the errors
#---------------------------------------------
#import unittest

# class TestJo(unittest.TestCase):
    # def test_sum(self):
        # self.assertTrue(type("moha") == str)

#IMPORTANT:
# if __name__ == '__main__':
    # unittest.main()
# if you won't do this code above
# you should do :
# python -m filename.py

# -----------------------------------------
# import unittest

# class TestA(unittest.TestCase):
    # def test_isupper(self):
        # self.assertEqual('hhh'.upper(), 'HHH')
# if __name__ == '__main__':
    # unittest.main()
# -----------------------------------------

#IMPORTANT: for following code use this 
#python -m doctest filename.py


# def add(x, y):
    # """
    # Add two num.
    # Usage:
    # >>> add(5,6)
    # 11
    # >>> add(1,22)
    # 35
    # """
    # return x+y
    
# def prt(name):
    # """
    # Add two num.
    
    # Usage:
    # >>> prt("habti")
    # 'habti'
    # """
    # return name

# print(prt("mohammed"))    
# print(add(5,6))
