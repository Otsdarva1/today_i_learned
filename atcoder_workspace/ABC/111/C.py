import math
r,g,b,n=map(int,input().split())

ans = 0
print()
for i in range(n//r):
    for j in range(n//g):
        for k in range(n//b):
            if i*r + j*g + k*b == n:
                ans += 1
print(ans)