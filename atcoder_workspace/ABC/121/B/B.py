n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for ai in a:
    absum = 0
    for i in range(m):
        absum += ai[i] * b[i]
    if absum + c > 0:
        ans += 1
print(ans)
