from random import *

def selection_sort(list1):
    for i in range(1,len(list1)):
        key = list1[i]
        j = i-1
        while j >= 0 and list1[j] > key:
            list1[j+1] = list1[j]
            j -= 1
        list1[j+1] = key
    return list1

if __name__ == "__main__":
    list1 = [randint(0,100) for i in range(20)]
    arr = selection_sort(list1)
    print(arr)