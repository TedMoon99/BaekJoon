# TGN
t = int(input())
for i in range(t):
    r, e, c = map(int, input().split())
    '''
    r : 광고를 하지 않았을 때의 수익
    e : 광고를 했을 때의 수익
    c : 광고 비용
    '''
    advantage = e - c
    if r == advantage:
        print("does not matter")
    elif r > advantage:
        print("do not advertise")
    else:
        print("advertise")
