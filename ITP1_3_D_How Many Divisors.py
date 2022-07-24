num_list = [int(x) for x in input().split()]

divisors = 0

for i in range(num_list[0], num_list[1]+1):
    if num_list[2] % i == 0:
        divisors += 1

print(divisors)

# https://www.javadrive.jp/python/function/index6.html