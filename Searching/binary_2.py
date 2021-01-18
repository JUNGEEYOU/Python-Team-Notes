def binary_search(array=list(), target=int()):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif target > array[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return None

array=[-1, 0 , 3, 5, 9, 12]     # 정렬된 리스트!

result = binary_search(array=array, target=9)
if result:
    print(result)
else:
    print("없다.")