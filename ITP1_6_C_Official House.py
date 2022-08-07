import numpy as np

ans = np.zeros((12, 10))

length = int(input())
num_list = list()
ans = []

for i in range(length):
    tmp_list = [x for x in input().split()]
    ans[(tmp_list[0]-1)*3+(tmp_list[1]-1)][tmp_list[2]-1] += tmp_list[3]

for i in range(12):
    for num in ans[i]:
        if num == ans[i][-1]:
            print(num)
            break
        print(num, end=" ")
    if i % 3 == 2 and not i == 11:
        print("####################")

# 二次元配列 python  https://camp.trainocate.co.jp/magazine/python-two-dimensional-array/