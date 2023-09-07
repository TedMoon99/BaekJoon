# 상근이의 친구들
while True:
    male, female = map(int, input().split())
    if not male and not female:
        break
    print(male + female)
