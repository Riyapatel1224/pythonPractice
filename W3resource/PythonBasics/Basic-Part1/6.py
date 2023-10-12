'''Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')'''

# num1=(input())
# li=list(num1)
# for i in li:
#     if i==',':
#         li.remove(i)
# tu=tuple(li)
# print(f"list: {li}")
# print(f"Tuple: {tu}")

num1=(input())
li=num1.split(',')
tu=tuple(li)
print(f"list: {li}")
print(f"Tuple: {tu}")