class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
       # count all freq of tasks, dict
       # get all the values of the taks
       # heapify the value

       # time tracking variable = 0
       # init a queue

       # while heap or q have something
        # increment time by 1

        #if nothing in heap, time is set to last interval

        # if heap, pop from the heap, decrement with +1, second value should be time + cooldown, push it to queue
        # if q and the top element in the queue is equal to the time, add it to the HEAP


        # return time

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            if not maxHeap:     # No tasks are ready to run right now
                time = q[0][1]  # Jump time forward to when the next task becomes available
            else: 
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])  
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

