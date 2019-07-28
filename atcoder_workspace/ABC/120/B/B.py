a, b, k = map(int, input().split())
tar = []
r = min(a, b)
for i in range(1, r + 1):
    if a % i == 0 and b % i == 0:
        tar.append(i)
print(tar[-k])
