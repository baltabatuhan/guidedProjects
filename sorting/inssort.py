my_list = [8, 2, 5, 4, 1, 3]


def insertion_sort(unsorted_list):
    sorted_list = []

    for n in unsorted_list:
        for i in range(len(sorted_list) - 1, -1, -1): #start,stop,step
            if sorted_list[i] < n:


    return sorted_list


sorted_list = insertion_sort(my_list)
