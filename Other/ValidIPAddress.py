'''
String: return combination of valid IP addresses in sorted order -  https://www.interviewbit.com/problems/valid-ip-addresses/

Given a string containing only digits, restore it by returning all possible valid IP address combinations.
A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

Example:
Given “25525511135”,
return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)
'''


class Solution:
    # @param A : string
    # @return a list of strings
    # TC - O(N^3), SC - O(N), where N= len(input)
    def restoreIpAddresses(self, A):

        def validity(str):
            if 0 <= len(str) <= 3:

                if len(str) > 1 and str[0] == "0":
                    return False

                if 0 <= int(str) <= 255:
                    return True

            return False

        N = len(A)
        ans = []

        # combination of 3 dots (i,j,k) between strings- A: [0, i], B: [i+1,j], C: [j+1,k], D: [k+1:]
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    a, b, c, d = A[: i + 1], A[i + 1: j + 1], A[j + 1: k + 1], A[k + 1:]

                    if validity(a) and validity(b) and validity(c) and validity(d):
                        IP = (a + "." + b + "." + c + "." + d)
                        ans.append(IP)

        return sorted(ans)


if __name__ == "__main__":
    str = "2552551100"
    out = Solution().restoreIpAddresses(str)
    print(out)
