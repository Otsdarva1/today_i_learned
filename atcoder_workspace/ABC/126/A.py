import sys
input = sys.stdin.readline
n, k = map(int, input().split())
s = input()

ans = ''
for i in range(1,n+1):
    if i == k:
        ans += s[i-1].lower()
    else:
        ans += s[i-1]
print(ans)