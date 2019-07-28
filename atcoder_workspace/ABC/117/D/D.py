m, f = 0, 0
n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(40, -1, -1):
  _sum = sum(map(lambda x: (x >> i) & 1, a))
  s = 0 if _sum > n//2 else 1 << i
  if not s or s > k - m:
    f += _sum << i
  else:
    f += n-_sum << i
    m += s
print(f)