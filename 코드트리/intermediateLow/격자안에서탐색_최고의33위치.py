def in_range(k, n):
    return 0 <= k <= n-3

n = int(input())
# 격자 생성
arr = []
# 격자 정보 받아오기
for _ in range(n):
    temp = input().split()
    tempArr = []
    for i in temp:
        tempArr.append(int(i))
    arr.append(tempArr)
print(arr)
print(arr[1][1])
# 정보 읽는 격자

