from random import *

def selection_sort(list1):
    for i in range(len(list1)-1):
        point = i 
        for j in range(i+1,len(list1)):
            if list1[point] > list1[j]:
                point = j
        list1[i],list1[point] = list1[point],list1[i]
    return list1

if __name__ == "__main__":
    list1 = [randint(0,100) for i in range(20)]
    arr = selection_sort(list1)
    print(arr)