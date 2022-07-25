num = int(input())

for i in range(num):
    if i % 3 == 0:
        print(i, end=" ")
        continue
    
    while True:
        if i % 10 == 3:
            print(i, end=" ")
            break
        i /= 10
        if i == 0:
            break
