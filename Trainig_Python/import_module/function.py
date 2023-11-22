def sign(a, b):
    if a*b > 0:
        print("have the same sign")
    else:
        print("not have the same sign")
def min(a, b):
    if a > b:
        print("the min is ", b)
    else:
        print("the min is ", a)
def max (a, b):
    if a > b:
        print("the max is ", a)
    else:
        print("the max is ", b)
#to show only when we compile function.py
if __name__ == "__main__":
    print("hey , from function")

    import sys

    script_n = sys.argv[0] # function.py
    arg = sys.argv[1:] # this all code after the function.py
    print("th script name ", script_n)
    print("the argv ", arg)
    
    sum = int(sys.argv[1]) + int(sys.argv[2])
    print(sum)