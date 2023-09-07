# 알람 시계

h, m = map(int, input().split())
# 0 <= h <= 23  | 0 <= m <= 59
minute = m - 45
if minute < 0:
    minute += 60
    if h == 0:
        h = 23
    else:
        h -= 1

print(h, minute)