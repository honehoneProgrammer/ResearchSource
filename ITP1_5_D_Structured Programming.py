num = int(input())

for i in range(1, num+1):
    if i % 3 == 0 or i % 10 == 3 or i // 10 == 3:
        print(i, end=" ")

# https://www.javadrive.jp/python/function/index6.html
