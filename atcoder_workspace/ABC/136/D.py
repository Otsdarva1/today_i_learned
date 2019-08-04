S = input()
N = len(S)

arr = [0] * N

R = 0
for i in range(N - 1):
    if S[i] == "R":
        R += 1
    if S[i + 1] == "L":
        arr[i + 1] += R // 2
        arr[i] += (R + 1) // 2
        R = 0

L = 0

for i in range(N - 1, 0, -1):
    if S[i] == "L":
        L += 1
    if S[i - 1] == "R":
        arr[i - 1] += L // 2
        arr[i] += (L + 1) // 2
        L = 0

# 配列の要素をスペース区切りで展開
print(*arr)