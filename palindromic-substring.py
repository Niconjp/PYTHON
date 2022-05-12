# https://leetcode.com/problems/longest-palindromic-substring/submissions/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        lst = []
        if len(s) == 1:
            return s
        elif len(s) == 0:
            return ""
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        elif len(set(s)) == 1:
            return s
        else:
            for n,l in enumerate(s):
                l2 = s[n+1::]
                for j in range(len(l2)):
                    if l2[j] == l:
                        lst.append(l+l2[:j+1])
            for x in range(len(lst)):
                if lst[x] == (lst[x][::-1]):
                    return lst[x]
