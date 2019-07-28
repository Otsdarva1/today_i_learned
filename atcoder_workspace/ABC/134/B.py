import sys
import math
input = sys.stdin.readline
n, d = map(int, input().split())
print(math.ceil(n/(2*d+1)))
