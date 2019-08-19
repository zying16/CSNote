def binary_search(array, item):
    start = 0
    end = len(array) - 1
    while start <= end:
        # 这两种写法是一样的，但 start + end 如果值很大容易溢出
        # mid = (start + end) // 2
        # 优化写法
        mid = start + (end - start) // 2
        if array[mid] == item:
            return True
        elif item < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False
