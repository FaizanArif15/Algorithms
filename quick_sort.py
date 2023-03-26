from random import *

def quick_sort(list1):
    if len(list1) <= 1:
        return list1
    small = []
    large = []
    pivot = list1[-1]
    for i in range(len(list1)-1):
        if list1[i] < pivot:
            small.append(list1[i])
        else:
            large.append(list1[i])
    return quick_sort(small) + [pivot] + quick_sort(large)

if __name__ == "__main__":
    list1 = [randint(0,100) for i in range(20)]
    arr = quick_sort(list1)
    print(arr)