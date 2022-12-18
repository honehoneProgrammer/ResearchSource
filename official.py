ans = [[0 for i in range(10)] for j in range(12)]
length = int(input())
num_list = list()

for i in range(length):
    tmp_list = [int(x) for x in input().split()]
    ans[(tmp_list[0]-1)*3+(tmp_list[1]-1)][tmp_list[2]-1] += tmp_list[3]

for i in range(12):
    if i % 3 == 2 and not i == 11:
        print("####################")