num = int(input())
H, M, S = (60*60), 60, 1
h = num // H
num -= h * H

m = num // M
num -= m * M

s = num // S
num -= s * S

print(h, m, s, sep=":")