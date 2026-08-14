class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # Solution 1 - Sort O(n log n) / O(n)
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq = []
        for num, cnt in count.items():
            freq.append([cnt, num])
        freq.sort()

        res = []
        while len(res) < k:
            res.append(freq.pop()[1])
        return res
 
        # Solution 2 - Heap O(n log k) / O(n log k)
 
        # Solution 3 - Bucket sort O(n) / O(n)

        