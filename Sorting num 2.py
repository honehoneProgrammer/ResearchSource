num_list = []
inp = input()

for i in inp.split():
    num_list.append(int(i))

min = 100000
ans = []

for j in range(len(num_list), 0,-1):
    min = 100000
    for i in range(j):
        if min > num_list[i]:
            min = num_list[i]
    ans.append(min)

print(ans[0], ans[1], ans[2])

