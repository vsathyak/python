#List operations

colourList=["white","Black","Orange","Blue","Red","Brown"]

print("First index item:",colourList[0])
print("First Three index item:",colourList[0:2])
print("List last item:",colourList[-1])
print("List from 2nd index to last:", colourList[2:])

#Change first index item
colourList[0]="Yellow"
print("Updated list:", colourList)

# change 2nd to 4th items
colourList[1:4] = [3, 5, 7]
print("Updated list:", colourList)

#Add item to a list
colourList.append("Sky Blue")
print("Updated list:", colourList)

#Add multiple item to the list
colourList.extend(["item1","item2","item3"])
print("Updated list:", colourList)
print("Update list using +", colourList+["gold","ash"])

#Remove item from list
del colourList[0]
print("First item deleted(Yellow):", colourList)

#Remove specific item from list
colourList.remove('item1')
print("Item name item1 is removed:",colourList)

#Remove item using pop() method and print index value of that item
print(colourList.pop(0))

del colourList #-->remove entire item from  list
#colourList.clear() #--> clear entire list



