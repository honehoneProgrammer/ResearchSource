num_list = []

while True:
    num_list.append(input().split())

    num_list[-1][0] = int(num_list[-1][0])
    num_list[-1][1] = int(num_list[-1][1])

    if num_list[-1][0] == 0 and num_list[-1][1] == 0:
        break

for num in num_list:
    for i in range(num[0]):
        for j in range(num[1]):
            if i % 2 == 0:
                if j % 2 == 0:
                    print("#", end="")
                else:
                    print(".", end="")

            else:
                if j % 2 == 0:
                    print(".", end="")
                else:
                    print("#", end="")
        print()
    print()