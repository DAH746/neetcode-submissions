class Solution(object):
    def hasDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)

        if len(set_nums) < len(nums):
            return True
        return False