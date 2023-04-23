n,k=map(int,input().split())
l=[]
for i in range(5):
    l.append(map(int,input().split()))
l.sort(reverse=True)
print(l[k-1])