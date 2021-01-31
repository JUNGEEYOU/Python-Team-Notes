def quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a[0]
        low = [i for i in a[1:] if i <= pivot]
        high = [i for i in a[1:] if i > pivot]
        return quick_sort(low) + [pivot] + quick_sort(high)


array = [7, 5, 9, 0, 1, 6, 2, 4, 8]
array = quick_sort(array)
print(array)



