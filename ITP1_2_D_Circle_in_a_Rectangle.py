num_list = [int(x) for x in input().split()]


if (0 <= num_list[2]-num_list[4]) and (num_list[2]+num_list[4] <= num_list[0]):
    if (0 <= num_list[3]-num_list[4]) and (num_list[3]+num_list[4] <= num_list[1]):
        print("Yes")
        exit()

print("No")


# https://techacademy.jp/magazine/15831 break文のとき