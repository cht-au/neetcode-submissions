class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import defaultdict
        freq_dict = defaultdict(int)

        for num in nums:
            freq_dict[num] += 1

        
        res = list(freq_dict.items())
        res.sort(key=lambda x: x[1], reverse=True)
        


        # print(res)

        return [res[i][0] for i in range(k)]

        