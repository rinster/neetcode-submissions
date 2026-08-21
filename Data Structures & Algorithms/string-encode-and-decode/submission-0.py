class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
            
        # "5 # h e l l o 5 # w o r l d"
        # i 
        #    j
        res = []
        i = 0
        j = 0

        # when j  is a hash
        # our length is i:j
        # word = [j+1:j + length + 1]
        # append word to our res array

        while i < len(s):
            if s[j] == "#":
                length = int(s[i:j])
                word = s[j+1:j+length + 1]
                res.append(word)
                j += length + 1 # move to the next #hash sign
                i = j
            else:    
                j += 1
        

        return (res)
    
