num_list = []
while True:
    num_list.append(int(input()))
    if num_list[-1] == 0:
        break

del num_list[-1]

for i in range(len(num_list)):
    print("Case ", i+1, ": ", num_list[i], sep="")

# https://www.modis.co.jp/candidate/insight/column_98 listの使い方
# https://qiita.com/kenta1984/items/9423959e292a1e173bbc