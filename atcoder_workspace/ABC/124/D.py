import sys
input = sys.stdin.readline
n, k = map(int, input().split())
s = input()
kukan1=[]
kukan2=[]
oneseq=1
zeroseq=1
before=s[0]
for i in range(1,n):
    if s[i] == '1':
        if before == '1':
            oneseq += 1
        else:
            kukan1.append(zeroseq)
            oneseq = 1
    else:
        if before == '0':
            zeroseq += 1
        else:
            kukan2.append(oneseq)
            zeroseq = 1
    before = s[i]

if s[n-1] == '1':
    if before == '1':
        kukan2.append(oneseq)
    else:
        kukan2.append(1)
else:
    if before == '0':
        kukan1.append(zeroseq)
    else:
        kukan1.append(1)

print(kukan1)
print(kukan2)