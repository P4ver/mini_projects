# improt the module with ALIAS --------

import function as exp

exp.add(15, 200)
exp.sous(9,2)
exp.div(24,4)
exp.mult(9,6)

# import the module ---------------

import function

function.add(15, 200)
function.sous(9,2)
function.div(24,4)
function.mult(9,6)

# import specific function with ALIAS -----------

from function import div as q #give div an alias (q)

q(45,9)

# import specific function -----------

from function import add, div

add(15, 200)
div(24,4)

# import all function -----------------

from function import *

add(15, 200)
sous(9,2)
div(24,4)
mult(9,6)