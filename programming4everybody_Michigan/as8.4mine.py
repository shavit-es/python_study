fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    pieces=line.split()
    for piece in pieces:
        if piece in lst:
            continue
        lst.append(piece)
lst.sort()
print(lst)
