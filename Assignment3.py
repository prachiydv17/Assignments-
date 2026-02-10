"""
Write a python program to perform following operations on Tuples :
a) Create and access a Tuple
b) Nested Tuple
c) Repetition of Tuple
d) Concatenation of Tuples
"""

# a) Create and access a Tuple

Tupe1 = (10,20,30,40,50)
print("Tuple :", Tupe1)
print("First Element :", Tupe1[0])
print("Last Element :", Tupe1[-1])


# b) Nested Tuple

Tupe2 = (1,2,(3,4,5),6)
print("Nested Tuple :", Tupe2)
print("Access Nested Element :", Tupe2[2][1])


# c) Repetition of Tuple

Tupe3 = ('A','B')
Repeated_tuple = Tupe3*3
print("Original Tuple :", Tupe3)
print("Repeated Tuple :", Repeated_tuple)

# d) Concatenation of Tuples

Tupe4 = (100,200)
Tupe5 = (300,400)
Concatenated_tupe = Tupe4 + Tupe5
print("First Tuple :", Tupe4)
print("Second Tuple :", Tupe5)
print("Concatenated Tuple:", Concatenated_tupe)