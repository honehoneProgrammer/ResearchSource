num_list = [int(x) for x in input().split()]

print(num_list[0]//num_list[1], num_list[0]%num_list[1], '{:.5e}'.format(num_list[0]/num_list[1]))

# https://www.headboost.jp/python-print-handle-number-of-digits/