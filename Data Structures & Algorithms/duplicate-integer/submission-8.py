class Solution(object):
    def hasDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length_list = len(nums)
        list_dict = len(list(dict.fromkeys(nums)))

        if list_dict == length_list:
            return False
        return True