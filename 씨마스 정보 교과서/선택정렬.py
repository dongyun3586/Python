
def selection_sort(arr):
    비교 = 0
    교환 = 0
    for i in range(0, len(arr) - 1):
        기준 = i
        for j in range(i+1, len(arr)):
            비교 += 1
            if arr[j] > arr[기준]:
                기준 = j
        if 기준 != i:
            arr[i], arr[기준] = arr[기준], arr[i]
            교환 += 1
            print(f'교환 숫자: {arr[i]} ↔ {arr[기준]}')
        print('{0} 비교: {1}, 교환: {2}'.format(arr, 비교, 교환))
    print('비교: {0}, 교환: {1}'.format(비교, 교환))
    return arr
 
arr = [8, 19, 3, 7, 5, 25]
arr = [8, 19, 3, 7, 5, 25, 14]
arr = [3, 5, 7, 8, 14, 19, 25]
# print('*** 선택 정렬 ***')
print('초기 상태 : {0}'.format(arr)) # 정렬 전
print('완료 상태 : {0}'.format(selection_sort(arr))) # 정렬 전