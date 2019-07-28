import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
for _ in range(m):
    b, c = map(int, input().split())
    a.extend([c] * b)
    if len(a) > n * 2:
        break

a.sort(reverse=True)
print(sum(a[:n]))