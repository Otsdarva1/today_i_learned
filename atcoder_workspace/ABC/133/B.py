import sys
import math

input = sys.stdin.readline

n, d = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        t = 0
        for l in range(d):
            y = x[i][l]
            z = x[j][l]
            t += (y - z) ** 2
        if math.sqrt(t).is_integer():
            ans += 1
print(ans)
