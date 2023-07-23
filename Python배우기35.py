# 배수와 약수
def isfactor(a,b):
    if not b % a:
        return 'factor'
    elif not a % b:
        return 'multiple'
    else:
        return 'neither'

while True:
    a, b = map(int, input().split())
    if not a and not b:
        break
    result = isfactor(a,b)
    print(result)
    
