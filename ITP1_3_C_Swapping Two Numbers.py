num_list = []

while True:
    num_list.append(input().split())
    if (num_list[-1][0] == "0") and (num_list[-1][1] == "0"):
        break

del num_list[-1]

for num in range(num_list):
    print(num.sort())

# https://techacademy.jp/magazine/49549