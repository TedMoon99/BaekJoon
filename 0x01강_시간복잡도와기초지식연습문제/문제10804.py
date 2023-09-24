# 카드 역배치
# 1 ~ 20까지 숫자의 20장 카드 오름차순 

# 카드 재배열 함수 
def reversefun(a, b): # Index : a-1 ~ b-1
  if a == b:
    return
  else: # list 분할하기
    prevList = currentList[:a-1]
    tempList = currentList[a-1: b]
    nextList = currentList[b+1:]
    tempList.sort(reverse=True)
    return prevList + tempList + nextList
     
    
# LIST 20개 생성 INDEX = 0 ~ 19
currentList = []
for i in range(20):
  currentList.append(i+1)
print(f"현재의 currentList\n{currentList}\n")
# 입력 받아오기
for _ in range(10):
  a, b = map(int, input().split())
  # 함수 실행
  currentList = reversefun(a,b)
  print("-----구분선-----")
  print(f"현재의 currentList는 \n{currentList}\n")
  

# 카드들의 배치 한 번에 출력
for j in range(len(currentList)):
  print(currentList[j], end=' ')