"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []

        for i in intervals:
            events.append((i.start, 1))
            events.append((i.end, -1))
        
        events.sort()
    
        curr = 0
        ans = 0

        for time, event_type in events:
            curr += event_type
            ans = max(ans, curr)

        return ans
            
            
            