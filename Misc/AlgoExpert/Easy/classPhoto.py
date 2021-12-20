def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    backRowAssign = 'red' if redShirtHeights[0] > blueShirtHeights[0] else 'blue'

    if backRowAssign == 'red':
        for i in range(len(redShirtHeights)):
            if blueShirtHeights[i] >= redShirtHeights[i]:
                return False
    else:
        for i in range(len(redShirtHeights)):
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False

    return True

input = {
    "blueShirtHeights": [21, 5, 4, 4, 4, 4, 4, 4, 4],
    "redShirtHeights": [19, 2, 4, 6, 2, 3, 1, 1, 4]
}

possibility = classPhotos(input["blueShirtHeights"], input["redShirtHeights"])
print(possibility)
