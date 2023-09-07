# 팰린드롬인지 확인하기
# 팰린드롬 : 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어

pelindrome = input()
length = len(pelindrome)
s = 0
for i in range(length // 2):
    if pelindrome[i] != pelindrome[-i-1]:
        print(0)
        s += 1
        break
if not s:
    print(1)