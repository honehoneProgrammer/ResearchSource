num_list = []
inp = input()

for i in inp.split():
    num_list.append(int(i))

min = 100000
ans = []
l = len(num_list)

for j in range(l):
    min = 100000
    l2 = len(num_list)
    for i in range(l2):
        print(i)
        print(num_list)
        if min > num_list[i]:
            min = num_list.pop(i)
    ans.append(min)

print(ans[0], ans[1], ans[2])

