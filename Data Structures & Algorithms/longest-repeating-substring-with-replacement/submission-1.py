class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # init countmap, resCount, maxCharRef -> countMap[char], l pointer
        charMap = {}
        maxChar = 0 
        l = 0
        res = 0

        # for r loop to the len of str
        for r in range(len(s)):
            # count the chars
            charMap[s[r]] = 1 + charMap.get(s[r], 0)
            # update the max Char
            maxChar = max(charMap[s[r]], maxChar)
             
            # while right - left + 1 - maxCharAmt is greater than k
            while (r - l + 1) - maxChar > k:
                #reduce countMap of char on the left
                charMap[s[l]] -= 1
                # move left pointer forward
                l += 1
            # update the max res
            res = max(res, (r - l) + 1)
        
        #return res
        return res