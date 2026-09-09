class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ''

        for s in strs:
            new_str += str(len(s)) + '#' + s
        return new_str

    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        res = []
        while j < len(s):
            if s[j] == '#':
                wordLen = int(s[i:j])
                word = s[j + 1 : j + wordLen  +1]
                res.append(word)
                j += wordLen + 1
                i = j
            else:
                j += 1
        
        return res

