s = input()

if '1' in s and '0' in s:
    print(min(s.count('1'), s.count('0')) * 2)
else:
    print(0)
