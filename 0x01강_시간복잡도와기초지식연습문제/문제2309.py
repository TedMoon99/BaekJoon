# # 일곱 난쟁이를 찾아줘!!
# dwarf = []
# for _ in range(9):
#   dwarf.append(int(input()))
# # 일곱 난쟁이의 키의 합은 100이다.
# fakeSum = sum(dwarf) - 100
# fakeDwarf = []

# for i in range(len(dwarf)):
#   for j in range(i+1, len(dwarf)):
#     if dwarf[i] + dwarf[j] == fakeSum:
#       fakeDwarf.append(i)
#       fakeDwarf.append(j)

# print("-----구분선-----")
# if len(fakeDwarf) == 2:
#   # pop을 한 뒤에 리스트 재조정 => 문제 발생 => 어떻게 해결할것인가??
#   # i는 항상 j보다 작으므로 j-1을 pop해주면 된다.
#   dwarf.pop(fakeDwarf[0])
#   dwarf.pop(fakeDwarf[1]-1)
#   dwarf.sort()
#   for k in range(7):
#     print(dwarf[k])
# else:
#   print("가능한 경우가 여러가지입니다.")

# 성준이형 버전
# 입력 : 20 7 23 19 10 15 25 8 13
import itertools

키 = []
for i in range(9):
    키.append(int(input()))

조합 = itertools.combinations(키, 7)
for set in 조합:
    if sum(set) == 100:
        sorted_tuple = sorted(set, reverse = False)
        break

for i in sorted_tuple:
    print(i)