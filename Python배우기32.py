# 개표
population = int(input())
vote = input()
a, b = 0, 0
for i in range(population):
    if vote[i] == 'A':
        a += 1
    else:
        b += 1
if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')