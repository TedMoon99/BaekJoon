# 약수들의 합
while True:
    num = int(input())
    if num == -1:
        break
    s, divisor = ['1'], 1
    for i in range(2, num):
        if not (num % i):
            s.append(str(i))
            divisor += i
    if divisor == num:
        result = ' + '.join(s)
        print(f"{num} = {result}")
    else:
        print(f"{num} is NOT perfect.")