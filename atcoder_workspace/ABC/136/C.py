import sys
input = sys.stdin.readline
n = int(input())
h = list(map(int, input().split()))
ma = 0
ans = True
for hi in h:
    t = hi + 1
    if t < ma:
        ans = False
        break
    if ma < hi:
        ma = hi
if ans:
    print('Yes')
else:
    print('No')
