num_list = []

while True:
    num_list.append(input().split())
    if (num_list[-1][0] == "0") and (num_list[-1][1] == "0"):
        break

del num_list[-1]

for i in range(len(num_list)):
    num_list[i][0] = int(num_list[i][0])
    num_list[i][1] = int(num_list[i][1])


for num in range(num_list):
    print(num.sort())

# https://techacademy.jp/magazine/49549