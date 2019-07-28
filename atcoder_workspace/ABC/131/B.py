n, l = list(map(int, input().split()))
a = [0 for i in range(n)]
for i in range(n):
    a[i] = l + i
a.sort(key=lambda x: abs(x))
print(sum(a[1:]))
