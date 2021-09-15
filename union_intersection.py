def array_union_intersection(arr_one, arr_two):
    arr_one = set(arr_one)
    arr_two = set(arr_two)
    union = list(arr_one | arr_two)
    intersection = list(arr_one & arr_two)
    return union, intersection
