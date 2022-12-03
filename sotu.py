a, b, c= map(int, input().split())
if a > b:
    if a > c:
        max = a;
        if b > c:
            mid = b
            min = c
        else:
            mid = c
            min = b
    else:
        max = c
        mid = a
        min = b
elif a > c:
    max = b
    mid = a
    min = c
else:
    min = a
    max = b
    mid = c


print('{} {} {}'.format(min,mid,max))