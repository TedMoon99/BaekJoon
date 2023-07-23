# 주사위 게임
n = int(input())

score1, score2 = 100, 100
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        score2 -= a
    elif a < b:
        score1 -= b
    else:
        continue

print(f"{score1}\n{score2}")