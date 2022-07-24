num_list = []
operand = ""

while True:
    num_list.append(input().split())
    operand = num_list[-1][1]
    if operand == "?":
        break

for i in range(len(num_list)):
    num_list[i][0] = int(num_list[i][0])
    num_list[i][2] = int(num_list[i][2])

for num in num_list:
    if operand == "+":
        print(num[0]+num[2])

    elif operand == "-":
        print(num[0]+num[2])

    elif operand == "*":
        print(num[0]+num[2])

    elif operand == "/":
        print(num[0]+num[2])

    elif operand == "?":
        break