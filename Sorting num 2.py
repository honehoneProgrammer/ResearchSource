num_list = []
inp = input()

for i in inp.split():
    num_list.append(int(i))

if num_list[1] < num_list[2] < num_list[3]:
    print(num_list[1], num_list[2], num_list[3])