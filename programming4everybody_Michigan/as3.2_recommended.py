hrs = input("Enter Hours:")
rate = input("Enter Rates:")
try:
    h=float(hrs)
    r=float(rate)
except:
    print("Error, please enter numeric input")
    quit()
if h>40:
    nh=40+1.5*(h-40)
else:
    nh=h

pay=r*nh
print(pay)
