import bisect

def count_by_range(a, left_val, right_val):
    right_val = bisect.bisect_right(a, right_val)
    left_val = bisect.bisect_left(a, left_val)
    return right_val - left_val

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))