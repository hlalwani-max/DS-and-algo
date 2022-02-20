# https://www.algoexpert.io/questions/Product%20Sum

def productSum(array, total=0, depth=1):
    # Write your code here.
    total = 0
    for element in array:
        if type(element) is list:
            total += productSum(element, total, depth + 1)
        else:
            total += element

    return depth * total
