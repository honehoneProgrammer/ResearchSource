length = int(input())
num_list = {'S' : [], 'H' : [], 'C' : [], 'D' : []}
ans_list = {'S' : [], 'H' : [], 'C' : [], 'D' : []}
lis = ['S', 'H' ,'C' ,'D']

for i in length:
    tmp_list = [x for x in input().split()]
    num_list[tmp_list[0]].append(int(tmp_list[1]))


for i in 13:
    for index in lis:
        if not i in num_list[index]:
            ans_list[index].append(i)

for index in lis:
    for ans in ans_list[index]:
        print(index, ans)


# python list 検索 https://atmarkit.itmedia.co.jp/ait/articles/2012/18/news022.html
# python dict https://utokyo-ipp.github.io/3/3-1.html
# python 否定 条件 https://www.sejuku.net/blog/65070
