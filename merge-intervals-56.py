class Solution:
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Suppose n = length(intervals).
        
        # If intervals are in sorted order,
        # a linear time alg, O(length(intervals))
        # can return the merged covering sets
        # by comparing endpoints of neighboring intervals
        
        #so perhaps (a) sort intervals in ascending order by start_i, and then
        # (b) merge in linear time.
        
        #total runtime, for list of n intervals, would be
        # O(n log n + n) \leq O(n log n)
        
        intervals.sort(key = lambda interval: interval[0])
        merged = [intervals[0]]
        for interval in intervals[1:]:
            if merged[-1][-1] >= interval[0]:
                if merged[-1][-1] <= interval[-1]:
                    merged[-1][-1] = interval[-1]
                #else, the interval is a subset of the last entry in merged
            else:
                merged.append(interval)
        
        return merged
