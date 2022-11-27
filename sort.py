num_list = []
while True:
    num_list.append(int(input()))
    if num_list[-1] == 0:
        break

del num_list[-1]