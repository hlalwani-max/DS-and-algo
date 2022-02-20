# https://www.algoexpert.io/questions/Permutations
# O(n! * n * n) time, O(n! * n) space
# Idea- pick one element and add it to perm, remove that element from the array and repeat.
# For optimized method O(n! * n) time watch video explanation, finding permutations using swapping.
def getPermutations(array):
    permutations = []
    getPermutationsHelper(array, permutations, [])
    return permutations


def getPermutationsHelper(array, permutations, perm):
    if len(array) == 0 and len(perm) > 0:
        permutations.append(perm)
        return
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1:]
            newPerm = perm + [array[i]]
            getPermutationsHelper(newArray, permutations, newPerm)


arr = [1, 2, 3]
perms = getPermutations(arr)
print("Permutations for {}: {}".format(arr, perms));[[]]
