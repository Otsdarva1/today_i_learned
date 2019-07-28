import sys
input = sys.stdin.readline
a = list(map(int, input().split()))
a.sort()
print(sum(a[:2]))