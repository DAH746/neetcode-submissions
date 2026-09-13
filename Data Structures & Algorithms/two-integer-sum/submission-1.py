class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i, v in enumerate(nums):
            diff = target - v
            if diff in prev:
                return [prev[diff], i]
            prev[v] = i
        
