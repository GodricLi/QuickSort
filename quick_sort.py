# _*_ coding=utf-8 _*_


# 快速排序
def quick_sort(arr, first, last):
    if first >= last:
        return
    mid_value = arr[first]
    low = first
    high = last

    while low < high:
        while low < high and arr[high] >= mid_value:
            high -= 1  # 游标左移
        arr[low] = arr[high]

        while low < high and arr[low] < mid_value:
            low += 1
        arr[high] = arr[low]
        arr[low] = mid_value

    quick_sort(arr, first, low - 1)
    quick_sort(arr, low + 1, last)


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 55, 6, 3, 4, 5, 6]
    quick_sort(l, 0, len(l) - 1)
    print(l)