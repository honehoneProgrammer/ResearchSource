length = int(input())
num_list = [int(x) for x in input().split()]

num_list.reverse()

for ele in num_list:
    print(ele, end=" ")