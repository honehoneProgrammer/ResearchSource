num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1>num2:
    tmp = num2
    num2 = num1
    num1 = tmp

if num2>num3:
    tmp = num3
    num3 = num2
    num2 = tmp


print('%d %d %d' %(num1, num2, num3))