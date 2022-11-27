num_list = []

while True:
    num_list.append(input().split())

    num_list[-1][0] = int(num_list[-1][0])
    num_list[-1][1] = int(num_list[-1][1])

    if num_list[-1][0] == 0 and num_list[-1][1] == 0:
        break