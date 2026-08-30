class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_pointer = 0
        end_pointer = 0
        seen = set()
        n = len(s)
        res = 0

        if n == 0:
            return 0
        elif n == 1:
            return 1

        # print(s)
        while end_pointer < n:
            # print(start_pointer, end_pointer)
            if s[end_pointer] not in seen:
                seen.add(s[end_pointer])
                end_pointer += 1
                res = max(res, end_pointer - start_pointer)
            else:
                seen.discard(s[start_pointer])
                start_pointer += 1

        return res



# zxyzxyz
#  s
#    e