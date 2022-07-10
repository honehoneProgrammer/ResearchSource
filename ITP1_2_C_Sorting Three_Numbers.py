num_list = [int(x) for x in input().split()]

num_list.sort()

for x in range(len(num_list)):
    if x == (len(num_list)-1):
        print(num_list[x])
        break
    print(num_list[x], end=" ")
