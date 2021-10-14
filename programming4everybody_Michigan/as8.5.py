fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    fhand = line.rstrip()
    if fhand.startswith('From:'):
        pieces=fhand.split()
        print(pieces[1])
        count=count+1

print("There were", count, "lines in the file with From as the first word")
