num_list = []
operand = ""

while True:
    num_list.append(input().split())
    operand = num_list[1]
    num_list[0] = int(num_list[0])
    num_list[1] = int(num_list[1])

    match operand:
        case "+":
            print(num_list[0]+num_list[2])  

        case "-":
            print(num_list[0]+num_list[2])
        
        case "*":
            print(num_list[0]+num_list[2])

        case "/":
            print(num_list[0]+num_list[2])

        case "?":
            break