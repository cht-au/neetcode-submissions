class Solution:
    def isPalindrome(self, s: str) -> bool:
        r_p = 0
        l_p = len(s) - 1

        while r_p < l_p:
            if not s[r_p].isalnum():
                r_p += 1
                continue
            if not s[l_p].isalnum():
                l_p -= 1
                continue

            if s[r_p].lower() != s[l_p].lower():
                return False
            
            r_p += 1
            l_p -= 1

        return True        

        