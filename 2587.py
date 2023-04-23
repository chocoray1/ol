
l=[]
for i in range(5):
    l.append(int(input()))
l.sort()
print((l[0]+l[1]+l[2]+l[3]+l[4])//5)
print(l[2])
