# https://www.algoexpert.io/questions/Find%20Three%20Largest%20Numbers

def shiftUpdate(largestNumbers, num, idx):
    for i in range(idx+1):
        if i == idx:
            largestNumbers[i] = num
        else:
            largestNumbers[i] = largestNumbers[i+1]


def updateLargest(largetNumbers, num):
    if largetNumbers[2] is None or num > largetNumbers[2]:
        shiftUpdate(largetNumbers, num, 2)
    elif largetNumbers[1] is None or num > largetNumbers[1]:
        shiftUpdate(largetNumbers, num, 1)
    elif largetNumbers[0] is None or num > largetNumbers[0]:
        shiftUpdate(largetNumbers, num, 0)


def findThreeLargestNumbers(array):
    # Write your code here.
    largetNumbers = [None]*3

    for num in array:
        updateLargest(largetNumbers, num)

    return largetNumbers


arr = [18, 141, 541]
print(findThreeLargestNumbers(arr))
