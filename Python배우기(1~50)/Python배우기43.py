# Yangjojang of The year
t = int(input())
for j in range(t):
    s, l = [],[]
    n = int(input())
    for i in range(n):
        temp = input().split()
        s.append(temp[0])
        l.append(int(temp[1]))
    max_drink = max(l)
    max_school = l.index(max_drink)
    print(s[max_school])