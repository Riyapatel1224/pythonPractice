'''Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.'''

num=int(input("Enter a number: "))
if num<=17:
    diff=17-num
else:
    diff=(num-17)*2
print(f"The difference is {diff}")