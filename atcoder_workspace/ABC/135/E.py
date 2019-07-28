import sys
input = sys.stdin.readline
k = int(input())
x, y = map(int, input().split())
if k % 2 == 0 and (x + y) % 2 == 1:
    print('-1')
if k % 2 == 1 and (x + y) % 2 == 0:
    print('-1')

print(abs(x) + abs(y))
