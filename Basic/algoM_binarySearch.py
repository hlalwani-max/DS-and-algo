# https://www.algoexpert.io/questions/Binary%20Search

def binarySearch(array, target):
    # Write your code here.
    start, end = 0, len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1