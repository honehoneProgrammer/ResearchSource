ans = [[0 for i in range(10)] for j in range(12)]
length = int(input())
num_list = list()

for i in range(12):
    print(" ", end='')
    for j in range(10):
        if j == 9:
            print('%d' % ans[i][j])
            break
        print('%d' % ans[i][j], end=" ")
    if i % 3 == 2 and not i == 11:
        print("####################")