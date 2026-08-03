class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = []
        set_res = set()
        for index in range(len(nums) - 2):
            r_p = n - 1
            l_p = index + 1
            while r_p > l_p:
                if nums[r_p] + nums[l_p] + nums[index] == 0:
                    triplets = [nums[index], nums[l_p], nums[r_p]]
                    if tuple(triplets) not in set_res:
                        res.append([nums[index], nums[l_p], nums[r_p]])
                        set_res.add(tuple(triplets))

                    l_p += 1
                elif nums[r_p] + nums[l_p] + nums[index] > 0:
                    r_p -= 1
                else:
                    l_p += 1

        print(set_res)
        return res
        