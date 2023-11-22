tuple1 = (1, 2, 3)
tuple2 = ("apple", "banana", "cherry")
tuple3 = (1, "hello", 3.14)

print(tuple1[0])  # Output: 1
print(tuple2[1])  # Output: "banana"

concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, "apple", "banana")
#_____________________________

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    tna = tuple_a[0] + tuple_b[0]
    tnb = tuple_a[1] + tuple_b[1]
    return tna , tnb
tuple_a = (1, 89)
tuple_b = (88, 11)

new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))