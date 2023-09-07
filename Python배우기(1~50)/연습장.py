def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def is_comfortable(r,c):
    dir = [0, 1, 2, 3]
    dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0] # 차례대로 N S W E
    temp = []
    for vec in dir:
        x, y = r, c
        x, y = x + dxs[vec], y + dys[vec]
        if in_range(x, y) and arr[x][y]:
            temp.append('*')
    if len(temp) == 3:
        return True
    else:
        return False

n, m = map(int, input().split())
arr = [
    [0] * n
    for _ in range(n)
]
for _ in range(m):
    r, c = map(int, input().split())
    r, c = r - 1, c - 1
    arr[r][c] = 1
    if is_comfortable(r,c):
        print(1)
    else:
        print(0)


