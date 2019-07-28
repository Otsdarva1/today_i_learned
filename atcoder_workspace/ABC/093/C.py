import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())

ma = max(a, b, c)

at = (ma - a) // 2 * 2 + a
bt = (ma - b) // 2 * 2 + b
ct = (ma - c) // 2 * 2 + c

ans = 0
ans += (ma - a) // 2
ans += (ma - b) // 2
ans += (ma - c) // 2

dif = abs(ma - at) + abs(ma - bt) + abs(ma - ct)

if dif == 0:
    print(ans)
elif dif == 1:
    print(ans + 2)
else:
    print(ans + 1)
