class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += f"{len(string)}\n{string}"
        return encoded



    def decode(self, s: str) -> List[str]:
        # print('*----*')
        # print(s)
        # print('*----*')
        i = 0
        decoded = ""

        #5\nHello5\nWorld
        res = []
        while i < len(s):
            length = ""
            while s[i] != "\n":
                length += s[i]
                i += 1
            i += 1
            res.append(s[i:i+int(length)])
            i += int(length)

        return res

