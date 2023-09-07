# 그릇
# 같은 방향으로 포개기 => 높이 5cm 증가
# 다른 방향으로 포개기 => 높이 10cm 증가
plate = input()
height = 10
for i in range(1, len(plate)):
    if plate[i] == plate[i-1]:
        height += 5
    else:
        height += 10
print(height)