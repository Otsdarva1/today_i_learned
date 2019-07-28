a, b, c = map(int, input().split())

for i in range(1, b + 1):
    tmp = a * i % b
    if tmp == c:
        print('YES')
        exit()

print('NO')