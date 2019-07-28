a,b,c=map(int,input().split())
ans=0
while b >= a:
    if c == 0:
        break
    else:
        b = b-a
        c -= 1
        ans += 1
print(ans)