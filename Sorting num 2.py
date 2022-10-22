num_list = []
inp = input()

for i in inp.split():
    num_list.append(int(i))

if num_list[0] < num_list[1] < num_list[2]:
    print(num_list[0], num_list[1], num_list[2])

elif num_list[2] < num_list[1] < num_list[0]:
    print(num_list[2], num_list[1], num_list[0])

elif num_list[0] < num_list[2] < num_list[1]:
    print(num_list[0], num_list[2], num_list[1])

elif num_list[1] < num_list[0] < num_list[2]:
    print(num_list[1], num_list[0], num_list[2])

elif num_list[1] < num_list[2] < num_list[0]:
    print(num_list[1], num_list[2], num_list[0])

elif num_list[2] < num_list[0] < num_list[1]:
    print(num_list[2], num_list[0], num_list[1])