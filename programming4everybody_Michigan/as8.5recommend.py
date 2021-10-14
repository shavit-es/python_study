han = open('mbox-short.txt')

for line in han:
    line=line.rstrip()
    wds=line.split()
    # Guradian
#    if len(wds) < 1 (3으로 해도 됨) :
#        continue

#    if line == '':
#        continue
    if len(wds)<3 or wds[0] != 'From' :  #순서도 중요함
        continue
    print(wds[2])
