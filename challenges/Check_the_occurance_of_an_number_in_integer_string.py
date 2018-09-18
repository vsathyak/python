#Check the occurance of an number in integer string
#If the number is there print the index if not return -1
#eg: 77 occurs in 779988977 at index  0 and 7

import re
def searchme(A, B):
    n_occurence=A.count(B)
    ocurrences=-1
    ocurrences = [m.start() for m in re.finditer(str(B), str(A))]
    if not ocurrences:
        return(-1)
    else:
        return(ocurrences)

A=input("Enter the value")
B=input("Enter the value to be searched?")
result=searchme(A,B)
print("Index of the number:",result)