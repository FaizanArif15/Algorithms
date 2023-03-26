from random import *

def bubble_sort(list1):
    for i in range(len(list1)):
        for j in range(len(list1)-1-i):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
    return list1

if __name__ == "__main__":
    list1 = [randint(0,100) for i in range(20)]
    arr = bubble_sort(list1)
    print(arr)