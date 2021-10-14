name = input("Enter file:")
email = []
counter = dict()
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line = line.rstrip()
    if line.startswith('From:'):
        pieces=line.split()
        email.append(pieces[1])
for x in email:
    counter[x] = counter.get(x,0)+1

maxvalue = 0
maxkey = None
for key,value in counter.items():
    if value>maxvalue:
        maxvalue=value
        maxkey=key
print(maxkey,maxvalue)
