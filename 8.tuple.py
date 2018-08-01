#Tuple values cannot be remove or modify thats the diff btwn tuple and list
# tuples can be reassigned
#tuple can be created without parentheses also called tuple packing

#tuple with diff type values
my_tuple = ("a", "b", 1, 2, 3.5)
print(my_tuple)

#tuple with nested values
my_tuple = ("Geethu", [8, 4, 6], ("savio", "Alex", "Elisha"))
print("Tuple with nested index 1:", my_tuple[1])
print("Tuple with nested index 2:2:", my_tuple[2][2])

#tuple packing
my_tuple = 3, 4.6, "savio"
print("Type of my_tuple:", type(my_tuple))

#tuple unpacking
a, b, c = my_tuple
print(a)
print(b)
print(c)

#tuple with single value should be defined end with ,
my_tuple = ("hello",)
print("Type of my_tuple:", type(my_tuple))

# Print entire tuple value
my_tuple=('J', 'U', 'A', 'N')
print("Entire tuple value:", my_tuple[:])

#Items in the nested element can be changed
my_tuple = (1, 2, 3, [4, 5])
my_tuple[3][1] = 9
my_tuple[3][0] = 10
print("Updated value in the tuple",  my_tuple)

#+ operation
my_tuple_a=(1, 2, 3)
my_tuple_b=('a', 'b', 'c')
print ("+ operation in tuple:", my_tuple_a + my_tuple_b)

my_tuple = ('p','r','o','g','r','a','m','i','z')
del my_tuple

#Defined methods in tuple
#count(x)	Return the number of items that is equal to x
#index(x)	Return index of first item that is equal to x

my_tuple=('a', 'n', 'i', 'a', 'm', 'm', 'a')
print("Number of time a in the tuple:", my_tuple.count('a'))
print("Index value of n:", my_tuple.index('n'))