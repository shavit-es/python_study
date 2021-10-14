hrs = input("Enter Hours:")
h = float(hrs)
if h>40:
    h=40+1.5*(h-40)
rate = input("Enter Rates:")
r = float(rate)
pay = r * h
print(pay)
