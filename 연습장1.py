n, t = map(int, input().split())
#command = input()

# 행렬 받아오기
arr = []
for _ in range(n):
    a, b, c = map(int, input().split())
    arr.append([a, b, c])
print(arr)