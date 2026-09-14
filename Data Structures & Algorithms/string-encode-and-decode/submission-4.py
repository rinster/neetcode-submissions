class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ''

        for word in strs:
             enc += str(len(word)) + "#" + word
        return enc

    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        res = []
        while j < len(s):
            if s[j] == "#":
                wordLen = int(s[i:j])
                word = s[j + 1 : j + wordLen + 1]
                res.append(word)
                j += wordLen + 1
                i = j
            j += 1

        return res
