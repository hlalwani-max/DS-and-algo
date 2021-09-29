'''
String- https://www.interviewbit.com/problems/justified-text/

Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line.

Pad extra spaces ‘ ‘ when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.

Your program should return a list of strings, where each string represents a single line.

Example:
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
 Note: Each word is guaranteed not to exceed L in length.
'''


class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    # TC- O(N*N* M), N- number of words, M- character in words- Can be easily converted to O(N*M) if we pass words directly into giveJustifyText, SC- O(N+M)
    def fullJustify(self, bag, L):

        def giveJustifyText(arr, start, end, L):
            words = []
            ccount = 0

            # count char and make words arr
            tmp = start
            while tmp <= end:
                words.append(arr[tmp])
                ccount += len(arr[tmp])
                tmp += 1

            num_spaces = L - ccount

            # end - start below is (number of words - 1)
            if end - start + 1 == 1:
                return (words[0] + " " * num_spaces)
            else:
                space_each = num_spaces // (end - start)
                rem_space = num_spaces % (end - start)
                spaces = [space_each for i in range(end - start)]

            for i in range(end - start):
                if rem_space > 0:
                    spaces[i] += 1
                    rem_space -= 1
                else:
                    break

            res = ""

            # number of words - 1, leaving last to add it in the end
            for i in range(end - start):
                res += (words[i] + " " * spaces[i])

            # if length of words greater than zero
            if end - start + 1 > 0:
                res += words[-1]

            return res

        N = len(bag)
        if N == 0: return []
        res = []
        i, start = 0, 0
        count = 0
        reached = False
        while i < N:
            if reached:
                txt = giveJustifyText(bag, start, i - 1, L)
                res.append(txt)
                start = i
                count = 0
                reached = False
                continue

            if count + len(bag[i]) > L:
                reached = True
                continue

            count += (len(bag[i]) + 1)

            i += 1

        # manipulate end line
        str = ""
        for word in bag[start:]:
            str += (word + " ")

        str = str[:-1]
        res.append((str + " " * (L - len(str))))

        return res


if __name__ == "__main__":
    arr, L = ["am", "fasgoprn", "lvqsrjylg", "rzuslwan", "xlaui", "tnzegzuzn", "kuiwdc", "fofjkkkm", "ssqjig",
              "tcmejefj", "uixgzm", "lyuxeaxsg", "iqiyip", "msv", "uurcazjc", "earsrvrq", "qlq", "lxrtzkjpg",
              "jkxymjus", "mvornwza", "zty", "q", "nsecqphjy"], 16
    out = Solution().fullJustify(arr, L)
    # print(out)

    for item in out:
        print(item, len(item))
