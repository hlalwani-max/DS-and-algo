# https://www.algoexpert.io/questions/Bubble%20Sort
#  O(n2) time, O(1) space
def bubbleSort(array):
    # Write your code here.
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]

    return array