import sys
input = sys.stdin.readline
n, k = map(int, input().split())
ans = 0
for v in range(1, n+1):
    p = 1
    p *= 1/n
    while v < k:
        v = v * 2
        p *= 1/2
    ans += p
print(ans)