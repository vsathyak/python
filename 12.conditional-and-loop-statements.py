#if statement
a=10
b=5
if a > b :
    print("%d is greater than %d" %(a,b))

#if else statement
a="apple"
b="ball"
if a == b:
    print("%s is equal to %s " %(a,b))
else:
    print("%s is not equal to %s!!!:D" %(a,b) )

#range function with if
for i in range(0,51,5):
    print ("Multiple of 5 till 50:", i)

#if...elif...else Statement
a=-1
if a == 0:
    print ("Zero")
elif a > 0:
    print ("Positive Number")
else:
    print("Negative number")

#For loop
##Basic
values='a','b','c'
for i in values:
    print(i)
##For loop in list
colourList=["white","Black","Orange","Blue","Red","Brown"]
for i in colourList:
    print("Colours in list:!!!", i)
##for loop in matrix
from numpy import *
a = array([['Roy',80,75],
           ['John',75,80],
           ['Dave',80,80]])
for i in  range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])

#while statement
##print 1 to 10
n = 10
i = 1
while i <= n:
    print (i)
    i=i+1

#while loop with else
n = 10
i = 1
while i <= 5:
    print("Value is <=5:", i)
    i = i + 1
else:
    print("Value is >5:", i)