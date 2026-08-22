class Solution:
    def findMin(self, nums: List[int]) -> int:
        l_p = 0
        r_p = len(nums) - 1

        i = 0
        while r_p > l_p:
            i += 1
            mid = (r_p + l_p) // 2
            print(l_p, mid, r_p)
            if nums[mid] >= nums[r_p]:
                l_p = mid + 1
            elif nums[mid] <= nums[r_p]:
                r_p = mid
            


        return nums[r_p]
            # [4, 5, 0, 1, 2, 3, 4]
            # [3, 4, 5, 6, 0, 1, 2]

            # [1, 2, 3]
            # [2, 3, 1]
            # [3, 1, 2]