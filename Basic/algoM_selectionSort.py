# https://www.algoexpert.io/questions/Selection%20Sort
# O(n2) time, O(1) space
# Idea- find minimum element in array and move it to the beginning.
def selectionSort(array):
    # Write your code here.
    for i in range(len(array)):
        minIdx = findMinIndex(array, i)
        array[i], array[minIdx] = array[minIdx], array[i]

    return array


def findMinIndex(array, i):
    minIndex = i
    for i in range(i, len(array)):
        if array[i] < array[minIndex]:
            minIndex = i

    return minIndex

