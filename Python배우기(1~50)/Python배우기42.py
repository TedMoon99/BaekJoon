# Baseball
def make_score(sc1, sc2):
    global y, k
    y += sc1
    k += sc2
def who_won(y, k):
    if y > k:
        return 'Yonsei'
    elif y < k:
        return 'Korea'
    else:
        return 'Draw'

t = int(input())
for i in range(t):
    y, k = 0, 0
    for j in range(9):
        sc1, sc2 = map(int, input().split())
        make_score(sc1, sc2)
    result = who_won(y, k)
    print(result)