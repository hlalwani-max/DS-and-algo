class Solution:
    '''
    SC - O(2N)
    TC- O(2N)
    '''

    def rearrangeArray(self, nums):
        positives, negatives = [], []
        outputList = []
        target = 0

        # save positives and negatives to save the order
        for item in nums:
            if item > 0:
                positives.append(item)
            else:
                negatives.append(item)

            target += 1

        positiveFlag = True
        currPosIndex, currNegIndex = 0, 0
        lenPositives, lenNegatives = len(positives), len(negatives)

        # fill the desired list with desired positives and negatives (keep count of the position), and also keep switching between them
        while target > 0:
            if positiveFlag:
                if (currPosIndex < lenPositives):
                    outputList.append(positives[currPosIndex])
                    currPosIndex += 1
                    positiveFlag = False
            else:
                if (currNegIndex < lenNegatives):
                    outputList.append(negatives[currNegIndex])
                    currNegIndex += 1
                    positiveFlag = True
            target -= 1

        return outputList
