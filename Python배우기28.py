# 학점 계산
score = input()

if score[0] == 'A':
    if score[1] == '+':
        print(4.3)
    elif score[1] == '0':
        print(4.0)
    else:
        print(3.7)
elif score[0] == 'B':
    if score[1] == '+':
        print(3.3)
    elif score[1] == '0':
        print(3.0)
    else:
        print(2.7)
elif score[0] == 'C':
    if score[1] == '+':
        print(2.3)
    elif score[1] == '0':
        print(2.0)
    else:
        print(1.7)
elif score[0] == 'D':
    if score[1] == '+':
        print(1.3)
    elif score[1] == '0':
        print(1.0)
    else:
        print(0.7)
elif score[0] == 'F':
    print(0.0)