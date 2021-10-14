hrs = input("Enter Hours:")
rate = input("Enter Rates:")
try:
    h=float(hrs)
    r=float(rate)
except:
    print("Error, please enter numeric input")
    quit()

def computepay(h,r):
    if h>40:
        nh = 40 + 1.5 * (h - 40)
    else:
        nh = h
    return r*nh
p = computepay(h,r)
print("Pay",p)
