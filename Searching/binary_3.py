import bisect

def binary_search(array=list(), target=int()):
    index = bisect.bisect_left(array, target)
    if index < len(array) and array[index] == target:
        return index
    return None

array=[-1, 0 , 3, 5, 9, 12]     # 정렬된 리스트!

result = binary_search(array=array, target=13)
if result:
    print(result)
else:
    print("없다")