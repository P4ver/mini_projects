a = int(input("enter the num a = "))
b = int(input("enter the num b = "))

ch = input("enter the operation ")

if ch == "+":
    sum = a + b
    print("the sum is ", sum)
elif ch == "-":
    sous = a - b
    print("the sous is ", sous)
elif ch == "*":
    pr = a * b
    print("the product is ", pr)
elif ch == "/":
    if b != 0:
        div = a / b
        print ("the div is ", div)
    else:
        print("b should not be null")

# ------------------------------------------------
age = int (input("Enter the age of the citizen "))

vote = "Yeah, gentlmen" if age >= 18 else "Hell no, get out of here kid"
print(vote)

# or------
print ("Yeah, gentlmen" if age >= 18 else "Hell no, get out of here kid")

