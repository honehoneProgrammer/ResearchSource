num_list = [int(x) for x in input().split()]

num_list.sort()

for x in range(num_list):
    print(num_list[x], end=" ")
    if x == (len(num_list)-1):
        print(num_list[x])
