# 네번째 점
a = input().split()
b = input().split()
c = input().split()
d = []
if a[0] == b[0]:
    d.append(c[0])
    if a[1] == c[1]:
        d.append(b[1])
    else:
        d.append(a[1])
elif a[0] == c[0]:
    d.append(b[0])
    if b[1] == c[1]:
        d.append(a[1])
    else:
        d.append(c[1])
elif b[0] == c[0]:
    d.append(a[0])
    if a[1] == c[1]:
        d.append(b[1])
    else:
        d.append(c[1])
else:
    print("Wrong")
print(d[0], d[1])