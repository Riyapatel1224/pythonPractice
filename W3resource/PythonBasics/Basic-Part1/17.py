# Write a Python program to test whether a number is within 100 of 1000 or 2000.

'''def absNum(num):
    diff=0
    if num<=1000:
        diff=1000-num
        if diff<=100:
            return True
        else:
            return False
    elif num>2000:
        diff=2000-num
        if diff<=100:
            return True
        else:
            return False


num=int(input("Enter a number: "))
num=absNum(num)
print(num)'''


def absNum(num):
    return(((1000-num)<=100) or ((2000-num)<=100))
num=int(input("Enter a number: "))
print(absNum(num))
