import sys
input = sys.stdin.readline
a, b = map(int, input().split())
ans=0
if a>b:
    ans+=a
    a+=-1
else:
    ans+=b
    b+=-1
ans+=max(a,b)
print(ans)