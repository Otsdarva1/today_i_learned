import sys
input = sys.stdin.readline
n, a, b = map(int, input().split())

print(min(a*n, b))