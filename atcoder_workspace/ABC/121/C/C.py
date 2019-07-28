n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

shops = sorted(
    ab,
    key=lambda x: x[0]
)
paid = 0
for cost, stock in shops:
    num = min(m, stock)
    paid += num * cost
    m = m - num
    if m == 0:
        break
print(paid)