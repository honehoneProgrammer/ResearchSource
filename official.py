import numpy as np

ans = np.zeros((12, 10))

length = int(input())
num_list = list()
ans = []

for i in range(length):
    tmp_list = [x for x in input().split()]
    ans[(tmp_list[0]-1)*3+(tmp_list[1]-1)][tmp_list[2]-1] += tmp_list[3]

