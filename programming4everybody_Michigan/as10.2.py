name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
di=dict()
li=list()
handle = open(name)
for lines in handle:
    if lines.startswith('From'):
        pieces=lines.split()
        lines.rstrip()
        if len(pieces)<3 :
            continue
        timepiece=pieces[5]
        time=timepiece.split(':')
        di[time[0]]=di.get(time[0],0)+1
li=sorted(di.items())
for (k,v) in li:
    print(k,v)
    
