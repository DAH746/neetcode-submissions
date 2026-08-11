class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        cs=set()

        for r in range(len(s)):
            while s[r] in cs:
                cs.remove(s[l])
                l+=1
            cs.add(s[r])
            res=max(res, r-l+1)
        return res
