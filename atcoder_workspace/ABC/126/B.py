import sys
input = sys.stdin.readline
s = input()
s1 = int(s[:2])
s2 = int(s[2:])
isS1YYMM = 1 <= s1 <= 12
isS2MMYY = 1 <= s2 <= 12
if isS1YYMM:
    if isS2MMYY:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if isS2MMYY:
        print("YYMM")
    else:
        print('NA')