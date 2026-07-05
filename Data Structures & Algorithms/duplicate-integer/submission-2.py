class Solution(object):
    def hasDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        list_dict = list(dict.fromkeys(nums))

        if len(list_dict) == len(nums):
            return False
        return True