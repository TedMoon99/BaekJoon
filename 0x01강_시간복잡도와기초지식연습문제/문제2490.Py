# 윷놀이
# 배 = 0, 등 = 1
# 도, 개, 걸, 윷, 모
check = 0
# input
for _ in range(3):  
  stick = input().split()
  check = stick.count('0') # 배의 개수를 카운트
  if check == 0: # 모
    print('E')
  elif check == 1: # 도
    print('A')
  elif check == 2: # 개
    print('B')
  elif check == 3: # 걸
    print('C')
  elif check == 4: # 윷
    print('D')
  else:
    print("잘못된 입력입니다. 입력을 확인해주세요.")
    continue
    