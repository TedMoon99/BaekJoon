def in_range_col(k, n):
    return 0 <= k <= n - 3

def in_range_row(j, n):
    return 0 <= j <= n - 3

def check(arr, k, j): # 3 x 3 격자 체크
    cnt = 0
    for i in range(k, k+3):
        for t in range(j, j+3):
            if arr[i][t]:
                cnt += 1
    return cnt
                

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

# 격자 범위 안에서 돌기
countArr = []
k, j = 0, 0
while in_range_row(j, n) and in_range_col(k, n):
    if in_range_row(k, n):
        temp = check(arr, k, j)
        countArr.append(temp)
        j += 1
    else:
        k += 1
        j = 0

result = max(countArr)
print(result)



