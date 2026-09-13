class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        # you're iterating from the time array which is 1 banana/hour to the max number is bananan in a pile

        while l <= r:
            k = (l + r) // 2 # pick the middle speed        
            totalTime = 0

            # for each pile, we compute how many hours it takes to eat that pile at speed k
            # p / k - the exact full k sizd bites
            # math.ceil to round up 5/ 2 = 2.5 -> 3 hrs needed
            for p in piles:
                #totalTime += math.ceil(float(p) / k)
                totalTime += (p + k - 1) // k   # integer ceiling division - cleaner without floats
            if totalTime <= h:
                res = k
                r = k -1 # too fast, try smaller
            else: 
                l = k +1 # eating too slow, need faster
        return res