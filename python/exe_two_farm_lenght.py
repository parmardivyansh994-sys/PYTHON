'''
 2) write a program to accept length and width of two different farm from user. and find out & display which farm is bigger 
'''

lenght = float(input("enter the total lenght of farm1 :-"))
weight = float(input("enter the total lenght of farm1 :-"))

total1 = lenght*weight

print("*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*")

lenght = float(input("enter the total lenght of farm2 :-"))
weight = float(input("enter the total lenght of farm2 :-"))

total2 = lenght*weight

print(total1)
print(total2)

if total1>total2:
    print("total size is ",total2,"farm 1 is gratter!!!")
if total1<total2:
    print("total size is ",total1,"farm 2 is gratter!!!")
if total1==total2:
    print("both farms are sam ")

print(":) :) thank you :) :)")
