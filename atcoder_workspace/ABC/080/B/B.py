n = input()
digit_sum = sum(map(int, list(n)))
if int(n) % digit_sum == 0:
    print('Yes')
else:
    print('No')