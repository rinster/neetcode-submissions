class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)


        # Solution 1 - Sort O(n log n) / O(n)
        # freq = []
        # for num, cnt in count.items():
        #     freq.append([cnt, num])
        # freq.sort()

        # res = []
        # while len(res) < k:
        #     res.append(freq.pop()[1])
        # return res
 
        # Solution 2 - Heap O(n log k) / O(n log k) 
        # for num, cnt in count.items():
        #     heapq.heappush(heap, (count[num], num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap[1]))
        # return res

        # Solution 3 - Bucket sort O(n) / O(n)
        freq =[[] for i in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res= []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        