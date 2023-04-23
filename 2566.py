l=[]
m=0
a,b=0,0
for i in range(9):
    t=list(map(int,input().split()))
    l.append(t)
for i in range(9):
    for j in range(9):
        if l[i][j]>m:
            m=l[i][j]
            a=i
            b=j
print(m)
print(a+1,b+1)