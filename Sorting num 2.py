num_list = []
inp = input()

for i in inp.split():
    num_list.append(int(i))

min = 100000
ans = []


jl =  range(len(num_list))
jl.__reversed__

for j in jl:
    for i in range(j):
        if min > num_list[i]:
            min = num_list[i]
    ans.append(min)

