n = int(input())
a = list(map(int, input().strip().split()))
min1 = min(a)
min2 = min1

for i in a:
    amari = i % min1
    if amari != 0:
        if amari < min1:
            min1 = amari
lop = True
while lop:
    if min1 == min2:
        ans = min1
        lop = False
    elif min1 < min2:
        min2 = min2 % min1
        if min2 == 0:
            ans = min1
            lop = False
    elif min1 > min2:
        min1 = min1 % min2
        if min1 == 0:
            ans = min2
            lop = False
print(ans)