'''
wap to findout simple iterest 
formula= prn/100 
'''

p = 0
r = 0
n = 0

p = input("enter value of principal")
r = input("enter value of rate")
n = input("enter value of number of year")

p = int(p)
r = int(r)
n = int(n)

ans = p*r*n/100

print("interest value is..",ans)

