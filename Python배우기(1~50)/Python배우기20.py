# 윤년
n = int(input())
if (not( n % 4 ) and n % 100 != 0) or n % 400 == 0 :
    print(1)
else:
    print(0) 