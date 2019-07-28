n = int(input())
a = list(map(int, input().split()))

ans = 0


def d(ai,ans):
    if ai % 2 != 0:
        return ans
    ans += 1
    return d(ai / 2, ans)


for ai in a:
    ans=d(ai,ans)
print(ans)
