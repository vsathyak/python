# matrix is a two-dimensional data structure
#netsed list item count should be same , otherwise it wont be a matrix

sample_matrix = [['Elisha',80,95,85,90],['Alex',95,85,85,100],['Juan',80,80,80,90]]
print(sample_matrix)

#accessing elements in the array
print(sample_matrix[1][0])

#Slicing a matrix (start:end:increment)
#create a matrix is using numpy library.
from numpy import *
a = array([['Roy',80,75,85,90,95],
           ['John',75,80,75,85,100],
           ['Dave',80,80,80,90,95]])
print(a[:3,[0,5]])
print(type(a))

#add a new raw to array
a = array([['Roy',80,75,85,90,95],
           ['John',75,80,75,85,100],
           ['Dave',80,80,80,90,95]])
a= append(a,[['Srika',80,85,90,95,100]],0) #ppend() method from numpy, 0 represent raw
print(a)

#add a new column
a = array([['Roy',80,75,85,90,95],
           ['John',75,80,75,85,100],
           ['Dave',80,80,80,90,95]])
a= insert(a,[2],[[73],[80],[85]],1) #2 for in which column value to be inserted, 1 represent column
print(a)

#Delete a raw
a = array([['Roy',80,75,85,90,95],
           ['John',75,80,75,85,100],
           ['Dave',80,80,80,90,95]])
a=delete(a,[1],0)
print("Raw element after deletion\n",a)

#Delete a column
a = array([['Roy',80,75,85,90,95],
           ['John',75,80,75,85,100],
           ['Dave',80,80,80,90,95]])
a=delete(a,s_[1:5],1)
print("Column elements after deletion\n",a)
