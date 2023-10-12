'''Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5 5+55+555
Expected Result : 615'''

# n=int(input("Enter a number: "))
# num=str(n)
# num2=num+num
# num3=num+num+num
# sum=int(num)+int(num2)+int(num3)
# print(f"{n}+{num2}+{num3}={sum}")

n=int(input("Enter a number: "))
n1=int("%s"%n)
n2=int("%s%s"%(n,n))
n3=int("%s%s%s"%(n,n,n))
print(n1+n2+n3)


