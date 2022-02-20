class Solution:

    def fun(self, arr, val):
        indices = list()

        for ind, item in enumerate(arr):
            if item == val:
                indices.append(ind)
            elif isinstance(item, list):
                for i in self.fun(item,val):
                    indices.append([ind].append(i))
        return indices


sol = Solution()
print(sol.fun([[[1, 1], [2, 1]]], 2))
