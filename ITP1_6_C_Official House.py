ans = [[0 for i in range(10)] for j in range(12)]
length = int(input())
num_list = list()

for i in range(length):
    tmp_list = [int(x) for x in input().split()]
    ans[(tmp_list[0]-1)*3+(tmp_list[1]-1)][tmp_list[2]-1] += tmp_list[3]

for i in range(12):
    print(" ", end='')
    for j in range(10):
        if j == 9:
            print('%d' % ans[i][j])
            break
        print('%d' % ans[i][j], end=" ")
    if i % 3 == 2 and not i == 11:
        print("####################")

# 二次元配列 python  https://camp.trainocate.co.jp/magazine/python-two-dimensional-array/
# vscode python numpy 使えない  https://www.wantanblog.com/entry/2021/12/25/223145
# print 整数 出力 python https://creive.me/archives/31794/
#c