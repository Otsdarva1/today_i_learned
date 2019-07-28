import sys
input = sys.stdin.readline
n = int(input())
p = list(map(int, input().split()))
wcnt = 0

for i in range(n):
    if p[i] != i+1:
        wcnt += 1

if wcnt == 0 or wcnt == 2:
    print('YES')
else:
    print('NO')