class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # n is start of sequence if n - 1 is not 
        sequence_start = []
        nums_set = set(nums)
        for num in nums:
            if num - 1 not in nums_set:
                sequence_start.append(num)
        longest_seq = 0

        for num in sequence_start:
            seq_len = 1
            start = num
            while start + 1 in nums_set:
                seq_len += 1
                start += 1
            longest_seq = max(longest_seq, seq_len)

        return longest_seq

        