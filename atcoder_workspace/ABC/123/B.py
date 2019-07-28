import sys
input = sys.stdin.readline

l1=[]
l2=[]
for _ in range(5):
    m = int(input())
    if m % 10 == 0:
        l1.append(m)
    else:
        l2.append([m, int(str(m)[-1])])

l2 = sorted(l2, key=lambda x: x[1], reverse=True)
ans = sum(l1)
for i in range(len(l2)):
    if i+1 != len(l2):
        ans += l2[i][0]+10-l2[i][1]
    else:
        ans += l2[i][0]

print(ans)