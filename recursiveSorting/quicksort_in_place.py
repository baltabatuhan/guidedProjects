# In-place quicksort
#
# In-place means we don't allocate any other arrays. We just juggle elements
# around in the passed-in array.
#
#        1
#        p
# [3 2 1 5 9 8 7 6]
#                i
#          ^       ^
#         low    high
​


def quicksort(a):
    def quicksort_recursive(a, low, high):
        if low >= high:
            return


​
p = low  # Pivot index
​
# Partition step
​
for i in range(low, high):
    if a[i] < a[p]:
        # Swap element i with item to right of pivot
        a[p + 1], a[i] = a[i], a[p + 1]
​
# Swap pivot with element on its right
a[p + 1], a[p] = a[p], a[p + 1]
​
# At this point, the pivot is in its final spot, and the left and right
# partitions need to be sorted
​
quicksort_recursive(a, low, p)
quicksort_recursive(a, p + 1, high)
​
quicksort_recursive(a, 0, len(a))
​
a = [5, 9, 3, 7, 2, 8, 1, 6]
​
quicksort(a)
​
print(a)
