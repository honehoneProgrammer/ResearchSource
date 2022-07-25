num = int(input())
tmp = 0

for i in range(1, num+1):
    tmp = i
    if i % 3 == 0:
            print(tmp, end=" ")
            continue
    
    while i:
        if i % 10 == 3:
            print(tmp, end=" ")
            break
        i //= 10

# https://www.javadrive.jp/python/function/index6.html
