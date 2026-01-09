# write a program to convert given 3 digit amount into words
#input: 125 output:one saven five 

number = input("enter number of 3 digit...")
number = int(number)

first = number // 10 // 10
print(first)

second = number // 10 % 10
print(second)

last = number % 10
print(last)

words = ['zero','one','two','three','four','five','six','seven','eight','nine']
print(words[first]," ", words[second],"", words[last])

