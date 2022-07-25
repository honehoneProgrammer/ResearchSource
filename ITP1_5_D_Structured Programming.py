num = int(input())
tmp = 0

for i in range(1, num+1):
    tmp = i
    while i:
        if i % 3 == 0 or i % 10 == 3:
            print(tmp, end=" ")
        i //= 10

# https://www.javadrive.jp/python/function/index6.html
