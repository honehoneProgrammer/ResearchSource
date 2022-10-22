num_list = []
inp = input()

for i in inp.split():
    num_list.append(int(i))

min = 100000
ans = []

for j in range(len(num_list)):
    for i in range(j):
        if min > num_list[i]:
            min = num_list[i]

