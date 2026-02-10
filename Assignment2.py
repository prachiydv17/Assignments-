"""
Write a Python program to perform following operations on set :
a) Create and access set elements
b) Union of the elements
c) Intersection of the elements
d) Difference of the elements
"""

# a) Create and access set elements

set1 = {21,22,23,24,25}
set2 = {41,52,63,71,83}

print("Accessing Set 1 elements :")
for element in set1 :
    print(element)

print("Accessing Set 2 elements :")
for element in set2 :
    print(element)


# b) Union of the elements

union_set = set1.union(set2)
print("Union of Set1 and Set2 :", union_set)


# c) Intersection of the elements

intersection_set = set1.intersection(set2)
print("Intersection of Set1 and Set2 :", intersection_set)


# d) Difference of the elements

difference_set = set1.difference(set2)
print("Difference of Set1 and Set2 :", difference_set)