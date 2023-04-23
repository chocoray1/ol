def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def fib2(n):
    d={
        1:1,
        2:1
    }
    count=0
    for i in range(3, n+1):
        count=count+1
        d[i]=d[i-1]+d[i-2]
    return d[n],count
print(*fib2(int(input())))