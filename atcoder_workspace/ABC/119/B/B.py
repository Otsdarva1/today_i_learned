n=int(input())
rate=380000.0

ans=0
for _ in range(n):
    x,u=input().split()
    x=float(x)
    if u == 'BTC':
        ans+=x * rate
    else:
        ans+=x
print(ans)