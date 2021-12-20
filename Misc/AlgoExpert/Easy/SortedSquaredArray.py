def sortedSquaredArray(array):
    # Write your code here.
    result = [0 for _ in array]

    start = 0
    end = len(array) - 1

    ind = len(array) - 1
    while start <= end:
        if abs(array[start]) > abs(array[end]):
            result[ind] = array[start]
            start += 1
        else:
            result[ind] = array[end]
            end -= 1
        ind -= 1

    for i in range(len(result)):
        result[i] = result[i] ** 2

    return result


input = {
    "array": [-10, -5, 0, 5, 10]
}

result = sortedSquaredArray(input["array"])
print(result)
