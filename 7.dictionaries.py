#A dictionary has a key: value pair. key should be unique

# empty dictionary
my_dict = {}

#Access element from dictionary
my_dict = {'name':'Savio', 'age': 30}
print (my_dict['name'])
print(my_dict.get('age'))

#Key with multiple values
my_dict = {'name': 'John', 1: [2, 4, 3]}
print ("EG: Multiple Value:",my_dict[1])

#update value in dictionary
my_dict = {'name':'Savio', 'age': 30}
my_dict['name']="Alex"
my_dict['age']=29
print("Updated dictionary values:", my_dict)

# add item to dictonary
my_dict = {'name':'Dinkle', 'age': 22}
my_dict['nick_name']="paru"
print(my_dict)

#Delete an item using pop
my_dict={1:1,2:4,3:9,4:16}
print("Item with key 2 is removed which having value:", my_dict.pop(2))

# delete a particular item
my_dict={1:1,2:4,3:9,4:16}
del my_dict[4]
print ("Removed item with key 4",my_dict)
my_dict.clear() #Delete all item in dict

#Iterating Through a Dictionary
my_dict = {1:1, 2:4, 3:9, 4:16 }
for i in my_dict:
    print(my_dict[i])
