# TC- O(N), SC- O(1)
def isValidSubsequence(array, sequence):
    # Write your code here.
    indS = 0
    lenS = len(sequence)

    for i in range(len(array)):
        if indS < lenS and array[i] == sequence[indS]:
            indS += 1

    return indS == lenS


array, sequence = [5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]
print(isValidSubsequence(array, sequence))