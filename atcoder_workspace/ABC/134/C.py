# import sys
# input = sys.stdin.readline
# n = int(input())
# a = [int(input()) for _ in range(n)]
#
# max_i = 0
# max_num = 0
# for i in range(n):
#     if a[i] > max_num:
#         max_num = a[i]
#         max_i = i
#
# a.sort(reverse=True)
#
# for i in range(n):
#     if i != max_i:
#         print(max_num)
#     else:
#         print(a[1])

n,*a=map(int,open(0).read().split())
ma=max(a)
# 最大値のインデックスを取得
ma_index=a.index(ma)
for i in range(n):
    if i==ma_index:
        # 最大値を除いた配列の最大値を出力
        print(max(a[:i]+a[i+1:]))
    else:
        print(ma)