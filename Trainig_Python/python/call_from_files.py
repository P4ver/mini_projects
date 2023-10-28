'''
IMPORTANT :
you have to make a file inside the folder
called __init__.py
'''



# call specific function --------------------

from test_File.test import string

string()

# call using ALIAS --------------------

import test_File.test as bring

bring.string()

# we use improt name_folder.name_py_file--------------------

import test_File.test 

test_File.test.string()