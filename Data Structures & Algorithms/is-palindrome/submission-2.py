class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            while s[left].isalnum() is False and left < right:
                left += 1
            while s[right].isalnum() is False and right > left:
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left +=1
            right-=1
        return True

            


