class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_1 = 26*[0]
        freq_2 = 26*[0]

        for ch in s:
            freq_1[ord(ch) - ord('a')] += 1
        for ch in t:
            freq_2[ord(ch) - ord('a')] += 1

        print(freq_1)
        print(freq_2)
        return freq_1 == freq_2  

        