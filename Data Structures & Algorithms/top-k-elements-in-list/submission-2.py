class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import defaultdict
        freq_dict = defaultdict(int)

        for num in nums:
            freq_dict[num] += 1
        
        freq_group = [[] for _ in range(len(nums))]
        for number, frequency in freq_dict.items():
            freq_group[frequency - 1].append(number)

        pop_count = 0
        res = []
        
        for item in reversed(freq_group):
            while item:
                res.append(item.pop())
                pop_count += 1
                if pop_count == k:
                    return res
                    
        return []

        