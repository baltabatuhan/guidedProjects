"""
quicksort(a):
    ...
    ...
    quicksort(...)
​
[5 9 3 7 2 8 1 6]
​
[3 2 1] [5] [9 7 8 6]    Things sorted after this pass: 1
         ^
[2 1] [3] [5] [7 8 6] [9] Things sorted after this pass: 3
       ^   ^           ^
​
[1 2 3 4 5 6]
​
[1] [2 3 4 5 6]
​
[1] [2] [3 4 5 6]
​
[1] [2] [3] [4 5 6]
​
​
[5 3 2 4 1 8 7 6 9]
​
[3 2 4 1] [5] [8 7 6 9]
[2 1] [3] [4] [5] [7 6] [8] [9]
​
quicksort(a)
    if len(a) <= 1:
        return a
​
    Partitioning in quicksort:
​
    choose a number to be the _pivot_
       let's just choose the first number
​
    split the list into two lists:
        left one with the numbers less than the pivot
        right one with numbers greater than (or equal to) the pivot
​
    put the smaller numbers left of the pivot
    greater numbers right of the pivot
​
    return quicksort(left) + [pivot] + quicksort(right)
"""
​


def partition(a):
    left = []
    pivot = a[0]
    right = []


​
    for v in a[1:]:
        if v < pivot:
            left.append(v)
        else:
            right.append(v)
​
    return left, pivot, right
​


def quicksort(a):
    if len(a) <= 1:
        return a


​
    left, pivot, right = partition(a)
​
    return quicksort(left) + [pivot] + quicksort(right)
​
print(quicksort([5, 9, 3, 7, 2, 8, 1, 6])
