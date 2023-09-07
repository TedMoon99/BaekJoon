time, min = map(int, input().split()) # 현재 시각과 분을 받아온다
need_time = int(input()) # 필요한 시간을 분 단위로 받아온다.

temp = min + need_time 
while temp >= 60:
    temp -= 60
    time += 1
    if time == 24:
        time = 0

print(f"{time} {temp}")
# 정말로 똑바로 연동이 되었나??