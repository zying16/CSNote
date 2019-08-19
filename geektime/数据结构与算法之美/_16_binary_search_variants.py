# 第一个等于
def binary_search_left(array, value):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if value > array[mid]:
            start = mid + 1
        elif value < array[mid]:
            end = mid - 1
        else:
            if mid == 0 or array[mid-1] != value:
                return mid
            else:
                end = mid - 1
    return -1

# 最后一个等于
def binary_search_right(array, value):
    start = 0
    length = len(array)
    end = length - 1
    while start <= end:
        mid = start + (end - start) // 2
        if value > array[mid]:
            start = mid + 1
        elif value < array[mid]:
            end = mid - 1
        else:
            if mid == length - 1 or array[mid+1] != value:
                return mid
            else:
                start = mid + 1
    return -1

# 第一个大于等于
def binary_search_not_less(array, value):
    start = 0
    length = len(array)
    end = length - 1
    while start <= end:
        mid = start + (end - start) // 2
        if value > array[mid]:
            start = mid + 1
        else:
            if mid == 0 or array[mid-1] < value:
                return mid
            else:
                end = mid - 1
    return -1


# 第一个小于等于
def binary_search_not_greater(array, value):
    start = 0
    length = len(array)
    end = length - 1
    while start <= end:
        mid = start + (end - start) // 2
        if value < array[mid]:
            end = mid - 1
        else:
            if mid == length - 1 or array[mid+1] > value:
                return mid
            else:
                start = mid + 1
    return -1
