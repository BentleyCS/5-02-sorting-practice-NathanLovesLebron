import random

import items


def bubbleSort(items:list):
    swaps = 0
    comparisons = 0

    sorted = False
    while not(sorted):
        sorted = True
        x = 0
        y = 1
        for i in range(len(items)-1):
            comparisons+=1
            if items[y] < items[x]:
                T=items[x]
                items[x] = items[y]
                items[y] = T
                swaps+=1
                sorted = False
            x+=1
            y+=1
    return items, swaps, comparisons

def insertionSort(items: list):
    swaps = 0
    comparisons = 0
    for sorted in range(1,len(items)):
        for j in range(sorted-1,-1, -1):
            comparisons +=1
            if items[j] > items[j+1]:
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp
                swaps +=1
            else:
                break
    return items, swaps, comparisons







def selectionSort(items : list):
    swaps = 0
    comparisons = 0
    whole = len(items)
    for i in range(whole - 1):
        small = i
        for n in range(i + 1, whole):
            comparisons += 1
            if items[n] < items[small]:
                small = n
        temp = items[i]
        items[i] = items[small]
        items[small] = temp
        swaps += 1
    return items, swaps, comparisons



    

    return items, swaps, comparisons


y = [9,8,7,6,5,4,3,2,1]
print(bubbleSort(y.copy()))
print(insertionSort(y.copy()))
print(selectionSort(y.copy()))
print()
x = [x for x in range(50)]
random.shuffle(x)
print(bubbleSort(x.copy()))
print(insertionSort(x.copy()))
print(selectionSort(x.copy()))
