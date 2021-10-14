hrs = input("Enter Hours:")
try:
    h = float(hrs)
    try:
        if h>40:
            h=40+1.5*(h-40)
        rate = input("Enter Rates:")
        r = float(rate)
        pay = r * h
        print(pay)
    except:
        print ("Error, please enter numeric input")
except:
    print ("Error, please enter numeric input")
