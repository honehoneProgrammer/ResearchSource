num_list = []

while True:
    num_list.append(input().split())

    num_list[-1][0] = int(num_list[-1][0])
    num_list[-1][2] = int(num_list[-1][2])

    if num_list[-1][0] == 0 and num_list[-1][1] == 0:
        break

for num in num_list:
    for i in range(num[0]):
        for j in range(num[1]):
            print("#", end="")
        print()
    print("\n\n", end="")