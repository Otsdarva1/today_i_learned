n,m = map(int, input().split())
menu = set(range(1,m+1))
for i in range(n):
    k, *a = list(map(int,input().split()))
    menu = menu & set(a)
print(len(menu))