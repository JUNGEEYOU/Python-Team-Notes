

def insertion_sort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
            else:
                break
    print(a)


array = [7, 5, 9, 0, 1, 6, 2, 4, 8]
insertion_sort(array)