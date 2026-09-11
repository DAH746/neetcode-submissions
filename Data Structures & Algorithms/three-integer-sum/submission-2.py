class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, value in enumerate(nums):
            if value > 0:
                break

            if index > 0 and value == nums[index-1]:
                continue
            
            left, right = index+1, len(nums)-1

            while left<right:
                if value + nums[left] + nums[right] == 0:
                    res.append([value, nums[left], nums[right]])
                    left +=1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif value + nums[left] + nums[right] < 0:
                    left +=1
                elif value + nums[left] + nums[right] > 0:
                    right -= 1

        return res
