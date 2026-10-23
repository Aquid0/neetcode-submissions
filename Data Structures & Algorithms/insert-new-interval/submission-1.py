class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        s, e = newInterval[0], newInterval[1]
        overlapping = []

        for i in range(len(intervals)):
            curr_s, curr_e = intervals[i][0], intervals[i][1]
            if max(curr_s, s) <= min(curr_e, e):
                overlapping.append((intervals[i], i))

        if not overlapping:
            for i in range(len(intervals)):
                if intervals[i][0] > s:
                    intervals.insert(i, newInterval)
                    return intervals
            return intervals + [newInterval]

        merged_start = min(s, overlapping[0][0][0])
        merged_end = max(e, overlapping[-1][0][1])

        start_idx = overlapping[0][1]
        end_idx = overlapping[-1][1]

        return intervals[:start_idx] + [[merged_start, merged_end]] + intervals[end_idx + 1:]

        
