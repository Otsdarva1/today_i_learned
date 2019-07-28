n, m = map(int, input().split())
a = [input() for i in range(n)]
b = [input() for i in range(m)]

ans = 'No'
for i in range(n - m + 1):
    sel = []
    for j in range(n):
        sel.append(a[j][i: i + m])
    for k in range(n - m + 1):
        tar = sel[k:k + m]
        if b == tar:
            ans = 'Yes'
            break

print(ans)