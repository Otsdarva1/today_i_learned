import sys
input = sys.stdin.readline
n = int(input())
w = list(map(int, input().split()))

ans = float('inf')
for i in range(n):
    s1 = sum(w[:i+1])
    s2 = sum(w[i+1:])
    dif = abs(s1 - s2)
    if ans > dif:
        ans = dif
print(ans)