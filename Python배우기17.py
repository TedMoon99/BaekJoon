# 세 수
arrayMax_second = input().split()

currentMax, secondMax = arrayMax_second[0], arrayMax_second[0]
for i in range(len(arrayMax_second)):
    if currentMax <= arrayMax_second[i]: # 현재 최댓값보다 더 큰 값이 존재하는 경우
        secondMax = currentMax # 현재의 최댓값을 두번째 최댓값으로 넘겨줌
        currentMax = arrayMax_second[i] # 새로운 최대값을 현의 최ㅅ값으로 가져옴

    else: # 현재 최대값보다 더 작은 값이 나타난 경우 | 
        if secondMax < arrayMax_second[i]: # 현재 최대값보다는 작지만 두번째 최대값보다는 큰 경우
            secondMax = arrayMax_second[i]
        else: 
            if secondMax == currentMax and i < 2:
                secondMax = arrayMax_second[i]

print(currentMax, secondMax) 
        

