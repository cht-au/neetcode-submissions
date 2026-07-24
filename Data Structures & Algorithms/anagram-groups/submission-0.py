class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freqs_anagram = {}
        
        for string in strs:
            freq = [0] * 26

            for char in string:
                freq[ord(char) - ord('a')] += 1
            
            if tuple(freq) not in freqs_anagram:
                freqs_anagram[tuple(freq)] = [string]
            else:
                freqs_anagram[tuple(freq)].append(string)

        print(freqs_anagram)
        return list(freqs_anagram.values())

        