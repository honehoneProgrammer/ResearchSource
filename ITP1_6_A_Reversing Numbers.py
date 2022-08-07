length = int(input())
num_list = [x for x in input().split()]

num_list.reverse()
element = ""
for ele in num_list:
    element = ele
    if element == num_list[-1]:
        print(element, end="")
        break
    print(ele, end=" ")

# print(" ".join(num_list))