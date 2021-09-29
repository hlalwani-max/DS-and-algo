class Solution:
    def sanityCheck(self, str):
        str = str.split("+")[0]
        # str =
        return str.replace(".","")

    def uniqueEmails(self, emails) -> int:
        res = []
        count = 0
        for item in emails:
            pair = item.split("@")
            # # or pair[1].find(".") != len(pair[1])
            # if pair[1].find("+") >=0:
            #     continue
            pair[0] = self.sanityCheck(pair[0])
            res.append(pair[0]+"@"+pair[1])
            print(res)
        return len(set(res))


email_list = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(Solution().uniqueEmails(email_list))
