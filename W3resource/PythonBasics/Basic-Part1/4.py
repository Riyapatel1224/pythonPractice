'''4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504'''

r=float(input("Enter a number: "))
pi=3.14
area=pi*(r*r)
print(f"Area={str(pi* r**2)}")