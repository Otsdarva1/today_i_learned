n = int(input())
s = '-' + input()
mi = float('inf')
wcnt=0
ecnt=0
for i in range(1, n + 1):
    mi = min(mi, s[:i].count('W') + s[i + 1:].count('E'))
print(mi)
