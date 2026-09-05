class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ''
        for s in strs:
            enc += str(len(s)) + "#" + s
        return enc


    def decode(self, s: str) -> List[str]:
        i= 0
        j = 0
        res = []

        while i < len(s):
            
            if s[j] == "#":
                length = int(s[i :j])
                word = s[j + 1 : j + length + 1] 
                res.append(word)
                j += length + 1
                i = j
            else:
                j += 1
        return res
