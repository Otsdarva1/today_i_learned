import math
n, k = map(int, input().split())
a = ''.join(input().split())
ai = a.find('1')
print((ai + 1) // (k - 1) + math.ceil((n - ai+1) / (k - 1)))
