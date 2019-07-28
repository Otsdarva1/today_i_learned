import sys
input = sys.stdin.readline
a, b, t = map(int, input().split())

ans=0
for i in range(a, t+1, a):
    ans += b
print(ans)