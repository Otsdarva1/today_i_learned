import sys
input = sys.stdin.readline

n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]

ab.sort(key=lambda x: x[1])

sum = 0
for cost, limit in ab:
    sum += cost
    if sum > limit:
        print('No')
        break
else:
    print('Yes')
