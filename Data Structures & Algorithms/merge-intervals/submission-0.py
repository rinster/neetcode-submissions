class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1] # most recent interval
            if start <= lastEnd:
                # merge the largest 
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end]) # append itself

        return output