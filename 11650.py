n=int(input())
l=[]
for _ in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
l.sort()
for x,y in l:
    print(x,y)
