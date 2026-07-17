class Solution(object):
    def hasDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        if len(set(nums)) < length:
            return True
        return False