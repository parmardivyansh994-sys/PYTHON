# write a program to convert given minutes into hours and remaining minutes
# input : 150 minutes 
# output : 2 hours and 30 minutes 

hours = input("enter minute for coversation :")
hours = int(hours)

hour = hours // 60
minutes = hours % 60

print(hour,"hours",minutes,"hours")
