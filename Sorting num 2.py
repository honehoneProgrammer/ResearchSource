num_list = []
inp = input()

for i in inp.split():
    num_list.append(int(i))

num_list.sort()

print(num_list[0], num_list[1], num_list[2])

