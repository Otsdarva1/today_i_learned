r,g,b,n = map(int,input().split())
a = [0]*(n+1)
a[0] = 1
for i in [r,g,b]:
    for j in range(n+1-i):
        a[j+i]+=a[j]
print(a[n])