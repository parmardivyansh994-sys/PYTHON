'''
write a program to find out elder brother from given two brother's age. 
input=age 
find= elder brother age
'''
import sys
brother1 = (input("enter age of one person "))
print(brother1)

brother2 = (input("enter age of second person "))
print(brother2)

if brother1==brother2:
    print("both are same :")
    sys.exit()
if brother1>brother2:
    print("brother1 is bigger,and the age is :",brother1)
else:
    print("brother2 is bigger,and the age is :",brother2)

