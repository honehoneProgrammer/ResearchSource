a,b,c=input().split()

if a <= b and b <= c:
    print(a, b, c)
if a <= c and c <= b:
    print(a, c, b)
if b <= a and a <= c:
    print(b, a, c)

