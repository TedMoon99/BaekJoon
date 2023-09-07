# 0 = not cute / 1 = cute
# 준희가 귀여운지 아닌지 알아보자!
t = int(input())
c, nc = 0, 0
for i in range(t):
    wc = int(input())
    if wc:
        c += 1
    else:
        nc += 1
if nc > c:
    print("junhee is not cute!")
else:
    print("junhee is cute!")