
def selection_sort(arr):
    비교 = 0
    교환 = 0
    for i in range(0, len(arr) - 1):
        min_idx = i
        for j in range(0, len(arr)-1-i):
            비교 += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
                교환+=1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print('{0} 비교: {1}, 교환: {2}'.format(a), 비교, 교환)
    print('비교: {0}, 교환: {1}'.format(비교, 교환)
    return arr
 
arr = [8, 19, 3, 7, 5, 25]
# print('*** 선택 정렬 ***')
# print('초기 상태 : {0}\n'.format(arr)) # 정렬 전
selection_sort(arr)