#The collection of elements of a single data type, eg. array of int, array of string.

shopinglist=["apple", "orange", "pottato", "onion"]
print(shopinglist)
print(shopinglist[0]) #accessing single item
print(len(shopinglist)) #Length of arrary

shopinglist.append("mango") #adding an item to the array
print(shopinglist)

#Delete item from array
del shopinglist[1] # delete based on index number
print(shopinglist)

shopinglist.remove("mango") #Delete based on item name
print(shopinglist)

#concatinate two array
array_1=[1, 2, 3]
array_2=[3, 4, 5]
print(array_1+array_2)

#reverse and array
shopinglist.reverse()
print(shopinglist)