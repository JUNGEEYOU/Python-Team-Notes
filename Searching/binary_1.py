def binary_search(array=list(), target=int(), left=int(), right=int()):
    if left > right:
        return None
    mid = (left + right) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, right)
    else:
        return binary_search(array, target, left, mid - 1)

array=[-1, 0 , 3, 5, 9, 12]     # 정렬된 리스트!

result = binary_search(array=array, target=9, left=0, right=len(array) - 1)
if result:
    print(result)
else:
    print("없다.")