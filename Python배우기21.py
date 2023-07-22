#  평균점수
a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
if a < 40:
    a = 40
if b < 40:
    b = 40
if c < 40:
    c = 40
if d < 40:
    d = 40
if e < 40:
    e = 40
print((a+b+c+d+e) // 5)