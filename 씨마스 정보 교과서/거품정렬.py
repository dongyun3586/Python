def bubbleSort(arr):
    비교 = 0
    교환 = 0
    for i in range(0, len(arr)-1):          # 반복횟수 : (0, 5) = 5회
        for j in range(0, len(arr)-1-i):    # 반복횟수 : 5, 4, 3, 2, 1
            비교 += 1
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # 자리 바꿈
                교환 += 1
        print('{0} 비교: {1}, 교환: {2}'.format(arr, 비교, 교환))
    print('비교: {0}, 교환: {1}'.format(비교, 교환))
    return arr
 
arr = [8, 19, 3, 7, 5, 25]
arr = [8, 19, 3, 7, 5, 25, 14]
arr = [3, 5, 7, 8, 14, 19, 25]
print('*** 거품 정렬 ***')
print('초기 상태 : {0}\n'.format(arr)) # 정렬 전
bubbleSort(arr) # 정렬 후
