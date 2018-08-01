#A set is an unordered collection of items(soindexing have no meaning).
# Every element is unique (no duplicates) and must be immutable (which cannot be changed).
#However, the set itself is mutable. We can add or remove items from it.
#Sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.

my_set={1, 2, 3, 'ab', 'ab', 'c', ('Father','mother')}
print("my_set:",my_set)

#Create a empty set
my_empty_set= set()
print("Type of my_empty_set:", type(my_empty_set))

#add single item to set
my_set={'a', 'b', 'c'}
my_set.add('d')
print("My current set after adding single item using add:", my_set)

#add multiple item to set
my_set={1,2,3}
my_set.update("item")
print("My current set after adding multiple item using update:",my_set)

# Union is performed using | operator or using method union()
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("Print union of A and B set (using |) :", A | B)
#print("Print union of A and B set (using method) :", A.union(B))

#Intersection is performed using & operator or using method intersection()
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("Print intersection of A and B set (using &) :", A & B)
print("Print intersection of A and B set (using method intersection) :", A.intersection(B))


