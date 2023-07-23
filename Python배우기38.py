# OX 퀴즈
def make_score(answer):
    n = len(answer)
    current, temp = 0, 0
    for i in range(n):
        if answer[i] == 'O':
            temp += 1
            current += temp
        else:
            temp = 0
    return current

t = int(input())
for i in range(t):
    quiz = input()
    score = make_score(quiz)
    print(score)

