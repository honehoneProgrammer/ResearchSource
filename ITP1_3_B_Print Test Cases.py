num_list = []
while True:
    num_list.append(int(input()))
    if num_list[-1] == 0:
        break

del num_list[-1]

for i in range(len(num_list)):
    print("Case", i+1, ":", num_list[i])

# https://www.modis.co.jp/candidate/insight/column_98 listの使い方