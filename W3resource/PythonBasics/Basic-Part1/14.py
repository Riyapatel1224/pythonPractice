'''Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days'''

from datetime import date

fdate=date(2014, 7, 2)
ldate=date(2014, 7, 11)
remain_days=ldate-fdate
print(remain_days.days)