num = int(input())
H, M, S = (60*60), 60, 1
h, m, s = num // H, num // M, num // S
num -= h * H
num -= m * M
num -= s * S

print(h, m, s, sep=":")