num_list = []

while True:
    num_list.append(int(input().split()))
    if num_list[-1][0] == 0 and num_list[-1][1] == 0:
        break

del num_list[-1]

for num in range(num_list):
    print(num)