# _*_ coding=utf-8 _*_


"""
快速排序:
    通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比
    另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，
    整个排序过程可以递归进行，以此达到整个数据变成有序序列。
时间复杂度：
    快速排序的最坏运行情况是 O(n²)，比如说顺序数列的快排。但它的平摊期望时间是 O(nlogn)，
且 O(nlogn) 记号中隐含的常数因子很小，比复杂度稳定等于 O(nlogn) 的归并排序要小很多。
所以，对绝大多数顺序性较弱的随机数列而言，快速排序总是优于归并排序。
"""


def partition(arr, left, right):
    """
    1.从数列中挑出一个元素，称为 "基准"（pivot）;
    2.重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
      在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
    :param arr: 列表
    :param left: 挑出元素的index
    :param right: 列表最大index
    :return:
    """
    pivot = arr[left]
    while left < right:                                 # 列表最少存在2个元素
        while left < right and arr[right] >= pivot:     # 找到右边比pivot小的元素
            right -= 1
        arr[left] = arr[right]                          # 将在此元素放在left的位置
        while left < right and arr[left] <= pivot:      # 找到左边比pivot大的元素
            left += 1
        arr[right] = arr[left]                          # 将此元素放在right的位置
    arr[left] = pivot                                   # left=right,此元素已经归位
    return left


def quick_sort(arr, left, right):
    """
    3.递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；
    :param arr:
    :param left:
    :param right:
    :return:
    """
    if left < right:                                    # 列表最少存在2个元素
        mid = partition(arr, left, right)
        quick_sort(arr, left, mid - 1)
        quick_sort(arr, mid + 1, right)
    return arr


if __name__ == '__main__':
    li = [1, 2, 3, 4, 5, 55, 6, 3, 4, 5, 6]
    new_arr = quick_sort(li, 0, len(li) - 1)
    print(new_arr)
