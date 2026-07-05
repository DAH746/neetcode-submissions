class Solution(object):
    def hasDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(set(nums)) != len(nums)

        length_list = len(nums)
        list_dict = list(dict.fromkeys(nums))

        if len(list_dict) == length_list:
            return False
        return True