# 인공지능 시계

# 인공지능 오븐은 오븐구이가 끝나는 시간을 초 단위로 자동적으로 계산

# 훈제오리구이를 시작하는 시각(sec), 오븐구이를 하는 데 필요한 시간(sec) => 오븐구이가 끝나는 시각

# 첫줄 -> 현재 시각(A, B, C) | 두번째 줄 => 요리하는 데 필요한 시간(D/sec)
def artificial_clock():
    a, b, c = map(int, input().split())
    d = int(input())
    temp = c + d
    while temp >= 60:
        temp -= 60
        b += 1
    while b >= 60:
        b -= 60
        a += 1    
        if a == 24:
            a = 0
    return a, b, temp

while True:
    s = input()
    if s == 'go ahead':
        a, b, temp = artificial_clock()
        print(f"{a} {b} {temp}")
    elif s == 'stop':
        print("Program is end")
        break
    else:
        print("Did you forget \'go ahead\'?")