class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                s_lower = s[left].lower()
                s_right = s[right].lower()
                if s_lower == s_right:
                    left +=1
                    right -= 1
                    continue
                else:
                    return False

            if s[left].isalnum() is False:
                left +=1
            if s[right].isalnum() is False:
                right -= 1
        return True