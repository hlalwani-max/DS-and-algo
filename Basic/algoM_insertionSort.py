# O(n2) time, O(1) space
# Idea- pick element at index i and insert it the the array[start to i-1] considering it sorted.
def insertionSort(array):
    # Write your code here.
    for i in range(1, len(array)):
        insertion(array, i)

    return array


def insertion(array, i):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j - 1], array[j] = array[j], array[j - 1]

