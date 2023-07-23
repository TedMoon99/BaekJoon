# 사분면

sector1, sector2, sector3, sector4, axis = 0, 0, 0, 0, 0
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if not (x and y):
        axis += 1
    else:
        if x >0 and y>0:
            sector1 += 1
        elif x >0 and y < 0:
            sector4 += 1
        elif x <0 and y > 0:
            sector2  += 1
        else:
            sector3 += 1

print(f"Q{1}: {sector1}")
print(f"Q{2}: {sector2}")
print(f"Q{3}: {sector3}")
print(f"Q{4}: {sector4}")
print(f"AXIS: {axis}")