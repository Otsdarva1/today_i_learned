n, k = map(int, input().split())
a = list(map(int, input().split()))

# left = total = ans = 0
#
# for right in range(n):
#     total += a[right]
#     while total >= k:
#         total -= a[left]
#         left += 1
#     ans += left
#
# print(ans)

ans, total, r = 0, 0, 0
for l in range(n):
    while total < k:
        if r == n:
            break
        else:
            total += a[r]
            r += 1
    if total < k:
        break
    ans += n - r + 1
    total -= a[l]

print(ans)
