l=[0]*31
for _ in range(28):
    n=int(input())
    l[n]=1
for i in range(1,31):
    if l[i]==0:
        print(i)
