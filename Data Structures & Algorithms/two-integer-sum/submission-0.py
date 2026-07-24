class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}

        for index, num in enumerate(nums):
            if target - num in complement:
                return [complement[target - num], index]
            
            complement[num] = index 

        