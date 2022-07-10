num = int(input())
H, M, S = (60*60), 60, 1

num -= (h = num // H) * H
num -= (m = num // M) * M
num -= (s = num // S) * S

print(h, m, s, sep=":")