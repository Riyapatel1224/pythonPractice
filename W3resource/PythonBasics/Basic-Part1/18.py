# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.


num1 = int(input("Enter 1 number: "))
num2 = int(input("Enter 2 number: "))
num3 = int(input("Enter 3 number: "))

result = (num1 + num2 + num3) * 3 if num1 == num2 == num3 else num1 + num2 + num3
print(result)



# def sum_thrice(x, y, z):

#      sum = x + y + z
  
#      if x == y == z:
#       sum = sum * 3
#      return sum

# print(sum_thrice(1, 2, 3))
# print(sum_thrice(3, 3, 3))
