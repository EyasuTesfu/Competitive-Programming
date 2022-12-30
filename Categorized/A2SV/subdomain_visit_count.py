# problem link: https://leetcode.com/problems/subdomain-visit-count/description/
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cpdomains_dict = {}
        for i in cpdomains:
            num = ""
            j = 0
            while(j < len(i)):
                if i[j] == " ":
                    break
                num += i[j]
                j += 1
            parent_directories = [i[j + 1:]]
            while(j < len(i)):
                if i[j] == ".":
                    parent_directories.append(i[j+1:])
                j += 1
            for k in parent_directories:
                if k in cpdomains_dict:
                    cpdomains_dict[k] += int(num)
                else:
                    cpdomains_dict[k] = int(num)
        res = []
        for i in cpdomains_dict:
            res.append(str(cpdomains_dict[i]) + " " + i)
        return res
