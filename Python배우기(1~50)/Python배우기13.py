# @ : 3을 곱한다
# % : 5를 더한다
# # : 7을 뺀다

# 첫 줄 : 테스트 케이스의 개수 T
# 입력 : 정수 or 소수 첫째자리 & 0 이상 100 이하
# 연산자는 최대 3개
# 출력 : 각 테스트 케이스에 대하여 화성 수학식의 결과를 계산한 후, 소수점 둘째 자리까지 출력
def operator(num, n):
    if n == '@':
        num *= 3
    elif n == '%':
        num += 5
    elif n == '#':
        num -= 7
    else:
        print("Wrong operator!")
    return num

t = int(input())
for i in range(t):
    inputlist = input().split()
    num = float(inputlist[0])
    for i in range(len(inputlist) - 1):
        num = operator(num, inputlist[i+1])
    print("%0.2f"%num)