import sys
input = sys.stdin.readline
s = input()
f = True
b = ''
for i in s:
    if i == b:
        f = False
    b = i
if f:
    print('Good')
else:
    print('Bad')