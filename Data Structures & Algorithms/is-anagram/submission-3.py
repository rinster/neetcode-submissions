class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Solution 1: Brute Naive O(n log n) | O(1)
        #return sorted(s) == sorted(t)

        # Solution 2: Hash O(n + m) | O(n)
        # if len(s) != len(t):
        #     return False
        # countT, countS = {}, {}

        # for i in range(len(s)):
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        #     countS[s[i]] = 1 + countS.get(s[i], 0)

        # return countS == countT

        # Solution 3: Hash Table using Array O(n + m) | O(n)
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for num in count:
            if num != 0:
                return False
        return True


        